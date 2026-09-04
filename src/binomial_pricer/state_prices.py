from .probability_space import CoinTossSpace

def radon_nikodym_derivative(actual_space: CoinTossSpace, rn_space: CoinTossSpace) -> dict[str, float]:
    """
    Calculates the Radon-Nikodym derivative Z(omega) of the risk-neutral measure 
    with respect to the actual measure for every path omega in Omega.
    
    Uses the closed-form ratio of the two measures from Eq. (3.1.8).
    """
    if actual_space.n_periods != rn_space.n_periods:
        raise ValueError("Actual and risk-neutral spaces must have the same number of periods.")
    
    z_dict = {}
    for omega in actual_space.get_omega():
        h_count = omega.count('H')
        t_count = omega.count('T')
        
        ratio_p = rn_space.p / actual_space.p
        ratio_q = rn_space.q / actual_space.q
        
        z_dict[omega] = (ratio_p ** h_count) * (ratio_q ** t_count)
        
    return z_dict

def state_price_density(
    actual_space: CoinTossSpace,
    rn_space: CoinTossSpace,
    r: float,
    n_periods: int | None = None,
    z_dict: dict[str, float] | None = None,
) -> dict[str, float]:
    """
    Calculates the state price density zeta(omega), which is the Radon-Nikodym 
    derivative Z(omega) discounted by the money market account over N periods.
    
    Uses Eq. (3.1.9).

    If z_dict is provided (e.g. already computed once via
    radon_nikodym_derivative), it is reused instead of recomputed -- useful
    when the same Z(omega) is needed for several purposes without
    recalculating it from actual_space and rn_space each time.
    """
    if n_periods is None:
        n_periods = actual_space.n_periods

    if z_dict is None:
        z_dict = radon_nikodym_derivative(actual_space, rn_space)

    discount_factor = (1 + r) ** n_periods
    
    zeta_dict = {}
    for omega, z_val in z_dict.items():
        zeta_dict[omega] = z_val / discount_factor
        
    return zeta_dict

def price_via_state_prices(payoff_dict: dict[str, float], actual_space: CoinTossSpace, zeta_dict: dict[str, float]) -> float:
    """
    Calculates the time-zero no-arbitrage price of a derivative given its terminal 
    payoff V_N(omega), the state price density zeta(omega), and the actual measure P.
    
    Uses Eq. (3.1.10).
    """
    v0 = 0.0
    for omega, v_n in payoff_dict.items():
        v0 += v_n * zeta_dict[omega] * actual_space.probability(omega)
    return v0

def radon_nikodym_process(actual_space: CoinTossSpace, rn_space: CoinTossSpace) -> list[dict[str, float]]:
    """
    Calculates the Radon-Nikodym derivative process Z_n.
    
    Defined as the conditional expectation of the terminal Radon-Nikodym 
    derivative Z under the actual probability measure.
    Uses Eq. (3.2.1) and Definition 3.2.4 (Eq. (3.2.2)).
    """
    z_terminal = radon_nikodym_derivative(actual_space, rn_space)
    process = []
    for n in range(actual_space.n_periods + 1):
        z_n = actual_space.conditional_expectation(z_terminal, n)
        process.append(z_n)
    return process

def state_price_density_process(actual_space: CoinTossSpace, rn_space: CoinTossSpace, r: float) -> list[dict[str, float]]:
    """
    Calculates the state price density process zeta_n, which is the 
    Radon-Nikodym derivative process discounted at the risk-free rate.
    
    Uses Theorem 3.2.7 and Eq. (3.2.7).
    """
    z_process = radon_nikodym_process(actual_space, rn_space)
    zeta_process = []
    for n in range(actual_space.n_periods + 1):
        discount_factor = (1 + r) ** n
        zeta_n = {path: z_val / discount_factor for path, z_val in z_process[n].items()}
        zeta_process.append(zeta_n)
    return zeta_process

def price_step_via_state_density_process(payoff_dict: dict[str, float], actual_space: CoinTossSpace, zeta_process: list[dict[str, float]], step: int) -> dict[str, float]:
    """
    Calculates the arbitrage-free price V_n of a derivative at a specific step n 
    using the state price density process zeta_n and actual probability measure.
    
    Implements the third equality in Theorem 3.2.7, Eq. (3.2.6):
    V_n = (1 / zeta_n) * E_n[zeta_N * V_N].
    """
    n_periods = actual_space.n_periods
    if not (0 <= step <= n_periods):
        raise ValueError("Step must be between 0 and N.")
        
    zeta_n = zeta_process[step]
    zeta_N = zeta_process[n_periods]
    
    zeta_N_V_N = {w: zeta_N[w] * payoff_dict[w] for w in actual_space.get_omega()}
    expected_zeta_N_V_N = actual_space.conditional_expectation(zeta_N_V_N, step)
    
    v_n = {prefix: (1.0 / zeta_n[prefix]) * expected_zeta_N_V_N[prefix] for prefix in zeta_n}
    
    return v_n