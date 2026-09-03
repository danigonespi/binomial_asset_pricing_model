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

def state_price_density(actual_space: CoinTossSpace, rn_space: CoinTossSpace, r: float, n_periods: int = None) -> dict[str, float]:
    """
    Calculates the state price density zeta(omega), which is the Radon-Nikodym 
    derivative Z(omega) discounted by the money market account over N periods.
    
    Uses Eq. (3.1.9).
    """
    if n_periods is None:
        n_periods = actual_space.n_periods
        
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