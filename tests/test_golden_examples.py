import pytest
import math
from itertools import product
import numpy as np
from binomial_pricer.equity_model import BinomialStockModel
from binomial_pricer.payoffs import EuropeanCall, LookbackOption, EuropeanPut, AsianOption, Forward, DelayedAsianOption, Payoff, RunningAveragePut
from binomial_pricer.engines import PricingEngine, ReducedStateEngine
from binomial_pricer.probability_space import CoinTossSpace
from binomial_pricer.stochastic_properties import is_martingale, is_markov, is_submartingale, is_supermartingale, is_stopping_time, stop_process
from binomial_pricer.state_prices import radon_nikodym_derivative, state_price_density, price_via_state_prices, radon_nikodym_process, state_price_density_process, price_step_via_state_density_process
from binomial_pricer.optimal_investment import LogUtility, PowerUtility, solve_optimal_investment, solve_goal_probability_maximization
from binomial_pricer.american_engine import AmericanEngine
from binomial_pricer.random_walk import symmetric_random_walk_path, first_passage_time, first_passage_time_mgf, first_passage_time_distribution

def test_example_1_1_1(base_model):
    """Example 1.1.1: call strike=5 -> V0=1.20, Delta0=0.5."""
    result = PricingEngine().price(base_model, EuropeanCall(strike=5.0), n_periods=1)
    assert result.v0 == pytest.approx(1.20)
    assert result.delta0 == pytest.approx(0.5)

def test_exercise_1_3_derivative_equals_stock(base_model):
    """Exercise 1.3: V1=S1 (call strike=0) -> V0 must equal s0 exactly."""
    result = PricingEngine().price(base_model, EuropeanCall(strike=0.0), n_periods=1)
    assert result.v0 == pytest.approx(base_model.s0)
    assert result.delta0 == pytest.approx(1.0)

@pytest.mark.parametrize("delta0, gamma0", [(1.0, 1.0), (-2.0, 3.0), (0.5, -1.5), (10.0, -4.0)])
def test_exercise_1_2_no_arbitrage_at_fair_price(delta0, gamma0):
    """
    Exercise 1.2: at the fair price 1.20 (which coincides with V0 from Example (1.1.1),
    any portfolio of Delta0 shares + Gamma0 options yields exactly opposite X1(H) and
    X1(T) -- if one is positive the other is negative, never both >= 0 with one > 0.
    Verified for several arbitrary combinations of Delta0, Gamma0, not just one.
    """
    S1_H, S1_T, r, option_price = 8.0, 2.0, 0.25, 1.20
    cash = -4 * delta0 - option_price * gamma0
    X1_H = delta0 * S1_H + gamma0 * max(S1_H - 5, 0) + (1 + r) * cash
    X1_T = delta0 * S1_T + gamma0 * max(S1_T - 5, 0) + (1 + r) * cash
    assert X1_H == pytest.approx(-X1_T)
    assert not (X1_H > 1e-9 and X1_T >= -1e-9)
    assert not (X1_T > 1e-9 and X1_H >= -1e-9)

def test_example_1_2_4_lookback_option(base_model):
    """Exact values from Example 1.2.4 (Multi-period Lookback option)."""
    payoff = LookbackOption()
    result = PricingEngine().price(base_model, payoff, n_periods=3)

    assert result.value_grid["HHH"] == pytest.approx(0.0)
    assert result.value_grid["HHT"] == pytest.approx(8.0)
    assert result.value_grid["HTH"] == pytest.approx(0.0)
    assert result.value_grid["HTT"] == pytest.approx(6.0)
    assert result.value_grid["THH"] == pytest.approx(0.0)
    assert result.value_grid["THT"] == pytest.approx(2.0)
    assert result.value_grid["TTH"] == pytest.approx(2.0)
    assert result.value_grid["TTT"] == pytest.approx(3.50)

    assert result.value_grid["HH"] == pytest.approx(3.20)
    assert result.value_grid["HT"] == pytest.approx(2.40)
    assert result.value_grid["TH"] == pytest.approx(0.80)
    assert result.value_grid["TT"] == pytest.approx(2.20)

    assert result.value_grid["H"] == pytest.approx(2.24)
    assert result.value_grid["T"] == pytest.approx(1.20)

    assert result.v0 == pytest.approx(1.376)
    assert result.delta0 == pytest.approx(0.1733, abs=1e-3)

def test_example_1_3_1_put_state_reduction(base_model):
    """Exact values from Example 1.3.1 using state reduction v_n(s)."""
    payoff = EuropeanPut(strike=5.0)
    result = ReducedStateEngine().price(base_model, payoff, n_periods=3)

    assert result.value_grid[(3, 32.0)] == pytest.approx(0.0)
    assert result.value_grid[(3, 8.0)] == pytest.approx(0.0)
    assert result.value_grid[(3, 2.0)] == pytest.approx(3.0)
    assert result.value_grid[(3, 0.5)] == pytest.approx(4.50)

    assert result.value_grid[(0, 4.0)] == pytest.approx(0.864)

def test_example_1_3_2_lookback_state_reduction(base_model):
    """Exact values from Example 1.3.2 using state reduction v_n(s, m)."""
    payoff = LookbackOption()
    result = ReducedStateEngine().price(base_model, payoff, n_periods=3)

    assert result.value_grid[(3, 32.0, 32.0)] == pytest.approx(0.0)
    assert result.value_grid[(3, 8.0, 16.0)] == pytest.approx(8.0)
    assert result.value_grid[(3, 8.0, 8.0)] == pytest.approx(0.0)
    assert result.value_grid[(3, 2.0, 8.0)] == pytest.approx(6.0)
    assert result.value_grid[(3, 2.0, 4.0)] == pytest.approx(2.0)
    assert result.value_grid[(3, 0.5, 4.0)] == pytest.approx(3.50)
    assert result.value_grid[(0, 4.0, 4.0)] == pytest.approx(1.376)

def test_exercise_1_8_asian_option_state_reduction(base_model):
    """
    Exact values from Exercise 1.8 (Asian option).
    Validates that both the brute force engine and the state reduction engine
    converge to the same V0 of 1.216 using a running sum aggregate.
    """
    payoff = AsianOption(strike=4.0, n_periods=3)
    
    res_brute = PricingEngine().price(base_model, payoff, n_periods=3)
    res_reduced = ReducedStateEngine().price(base_model, payoff, n_periods=3)
    
    expected_v0 = 1.216
    
    assert res_brute.v0 == pytest.approx(expected_v0)
    assert res_reduced.v0 == pytest.approx(expected_v0)
    assert res_reduced.delta0 == pytest.approx(res_brute.delta0)

def test_exercise_2_2_expectations(base_model):
    """
    Exercise 2.2: Compute ES1, ES2, ES3 under risk-neutral (p=1/2) 
    and actual (p=2/3) probabilities.
    """
    rn_space = CoinTossSpace(n_periods=3, p=0.5)
    S1 = {w: base_model.price_path(w)[1] for w in rn_space.get_omega()}
    S2 = {w: base_model.price_path(w)[2] for w in rn_space.get_omega()}
    S3 = {w: base_model.price_path(w)[3] for w in rn_space.get_omega()}
    
    assert math.isclose(rn_space.expectation(S1), 4.0 * 1.25)
    assert math.isclose(rn_space.expectation(S2), 4.0 * (1.25**2))
    assert math.isclose(rn_space.expectation(S3), 4.0 * (1.25**3))
    
    act_space = CoinTossSpace(n_periods=3, p=2/3)
    assert math.isclose(act_space.expectation(S1), 4.0 * 1.5)
    assert math.isclose(act_space.expectation(S2), 4.0 * (1.5**2))
    assert math.isclose(act_space.expectation(S3), 4.0 * (1.5**3))

def test_exercise_2_4_random_walk_martingale():
    """Exercise 2.4: Symmetric random walk is a martingale."""
    space = CoinTossSpace(n_periods=3, p=0.5)
    
    process = []
    for n in range(4):
        if n == 0:
            process.append({"": 0.0})
            continue
            
        M_n = {}
        for seq in product("HT", repeat=n):
            path = "".join(seq)
            M_n[path] = sum(1.0 if coin == 'H' else -1.0 for coin in path)
        process.append(M_n)
        
    assert is_martingale(space, process)

def test_theorem_2_4_4_discounted_stock_is_martingale(base_model):
    """Theorem 2.4.4: Discounted stock price is a martingale under risk-neutral measure."""
    p_tilde, _ = base_model.risk_neutral_prob
    space = CoinTossSpace(n_periods=3, p=p_tilde)
    
    process = []
    for n in range(4):
        S_n = {}
        if n == 0:
            S_n[""] = base_model.s0
            process.append(S_n)
            continue
            
        for seq in product("HT", repeat=n):
            path = "".join(seq)
            prices = base_model.price_path(path)
            S_n[path] = prices[-1] / ((1 + base_model.r) ** n)
        process.append(S_n)
        
    assert is_martingale(space, process)

def test_example_2_5_4_running_maximum_is_not_markov(base_model):
    """
    Example 2.5.4: M_n = max S_k alone is NOT a Markov process.
    However, the two-dimensional state (S_n, M_n) IS Markov (per generalizations in 2.13).
    """
    space = CoinTossSpace(n_periods=3, p=2/3) 
    
    process_1d = []
    process_2d = []
    
    for n in range(4):
        M_n = {}
        M_n_2d = {}
        if n == 0:
            M_n[""] = base_model.s0
            M_n_2d[""] = (base_model.s0, base_model.s0)
            process_1d.append(M_n)
            process_2d.append(M_n_2d)
            continue
            
        for seq in product("HT", repeat=n):
            path = "".join(seq)
            prices = base_model.price_path(path)
            maximum = max(prices)
            M_n[path] = maximum
            M_n_2d[path] = (prices[-1], maximum)
            
        process_1d.append(M_n)
        process_2d.append(M_n_2d)
        
    assert not is_markov(space, process_1d)
    assert is_markov(space, process_2d)

def test_eq_2_3_2_and_2_3_5_risk_neutral_pricing_one_step(base_model):
    """
    Eq (2.3.2): (p_tilde*u + q_tilde*d) / (1+r) == 1
    Eq (2.3.5): S_n = 1/(1+r) * E_n[S_{n+1}] under risk-neutral measure.
    """
    p_tilde, q_tilde = base_model.risk_neutral_prob
    
    assert math.isclose((p_tilde * base_model.u + q_tilde * base_model.d) / (1 + base_model.r), 1.0)
    
    space = CoinTossSpace(n_periods=2, p=p_tilde)
    S_2 = {w: base_model.price_path(w)[-1] for w in space.get_omega()}
    
    E_1_S_2 = space.conditional_expectation(S_2, 1)
    
    for prefix in E_1_S_2:
        S_1 = base_model.price_path(prefix)[-1]
        assert math.isclose(S_1, (1 / (1 + base_model.r)) * E_1_S_2[prefix])

def test_theorem_2_4_5_discounted_wealth_is_martingale(base_model):
    """
    Theorem 2.4.5: Discounted wealth is a martingale under risk-neutral measure.
    Uses Eq. (2.4.6) and verifies Eq. (2.4.7).
    """
    N = 3
    call = EuropeanCall(strike=5.0)
    engine = PricingEngine()
    result = engine.price(base_model, call, n_periods=N)

    p_tilde, _ = base_model.risk_neutral_prob
    space = CoinTossSpace(n_periods=N, p=p_tilde)

    X = []
    for n in range(N + 1):
        X_n = {}
        if n == 0:
            X_n[""] = result.v0  
            X.append(X_n)
            continue

        for seq in product("HT", repeat=n):
            path = "".join(seq)
            prev_path = path[:-1]
            
            delta_n = result.delta_grid[prev_path]
            X_prev = X[n-1][prev_path]
            
            S_prev = base_model.price_path(prev_path)[-1] if prev_path else base_model.s0
            S_curr = base_model.price_path(path)[-1]

            X_n[path] = delta_n * S_curr + (1 + base_model.r) * (X_prev - delta_n * S_prev)
        X.append(X_n)

    discounted_X = []
    for n in range(N + 1):
        discounted_X.append({p: v / ((1 + base_model.r)**n) for p, v in X[n].items()})

    assert is_martingale(space, discounted_X)

def test_exercise_2_3_convex_function_of_martingale_is_submartingale():
    """
    Exercise 2.3: A convex function (phi(x) = x^2) applied to a martingale 
    results in a submartingale.
    """
    space = CoinTossSpace(n_periods=3, p=0.5)
    
    M = []
    for n in range(4):
        if n == 0:
            M.append({"": 0.0})
        else:
            M.append({ "".join(seq): sum(1.0 if c == 'H' else -1.0 for c in seq)
                       for seq in product("HT", repeat=n) })

    phi_M = []
    for n in range(4):
        phi_M.append({path: val**2 for path, val in M[n].items()})

    assert is_submartingale(space, phi_M)
    assert not is_martingale(space, phi_M)  

def test_exercise_2_4_geometric_symmetric_random_walk():
    """
    Exercise 2.4(ii): Verifies that the normalized geometric symmetric 
    random walk is a martingale.
    """
    space = CoinTossSpace(n_periods=3, p=0.5)
    sigma = 0.5
    normalization = 2.0 / (math.exp(sigma) + math.exp(-sigma))

    process = []
    for n in range(4):
        if n == 0:
            process.append({"": 1.0})
        else:
            S_n = {}
            for seq in product("HT", repeat=n):
                path = "".join(seq)
                M_n = sum(1.0 if c == 'H' else -1.0 for c in path)
                S_n[path] = math.exp(sigma * M_n) * (normalization ** n)
            process.append(S_n)

    assert is_martingale(space, process)

def test_exercise_2_8_risk_neutral_pricing_formula(base_model):
    """
    Exercise 2.8: Demonstrates that recursive algorithm pricing V_n (1.2.16) 
    exactly matches the risk-neutral conditional expectation Eq. (2.4.11).
    """
    N = 3
    payoff = LookbackOption()
    result = PricingEngine().price(base_model, payoff, n_periods=N)

    p_tilde, _ = base_model.risk_neutral_prob
    space = CoinTossSpace(n_periods=N, p=p_tilde)

    V_N = {path: result.value_grid[path] for path in space.get_omega()}

    for n in range(N):
        expected_V_N = space.conditional_expectation(V_N, n)
        discount_factor = (1 + base_model.r) ** (N - n)

        prefixes = [""] if n == 0 else ["".join(seq) for seq in product("HT", repeat=n)]
        for prefix in prefixes:
            v_n_martingale = expected_V_N[prefix] / discount_factor
            v_n_algorithmic = result.value_grid[prefix]
            assert math.isclose(v_n_martingale, v_n_algorithmic, abs_tol=1e-9)


def test_exercise_2_11_put_call_parity(base_model):
    """
    Exercise 2.11: Put-Call Parity properties for European Options and Forwards.
    Confirms C_n = F_n + P_n, and verifies static Forward pricing F_0.
    """
    N = 3
    K = 5.0
    
    engine = PricingEngine()
    res_c = engine.price(base_model, EuropeanCall(strike=K), n_periods=N)
    res_p = engine.price(base_model, EuropeanPut(strike=K), n_periods=N)
    res_f = engine.price(base_model, Forward(delivery_price=K), n_periods=N)

    for n in range(N + 1):
        prefixes = [""] if n == 0 else ["".join(seq) for seq in product("HT", repeat=n)]
        for p in prefixes:
            c_n = res_c.value_grid[p]
            expected_c_n = res_f.value_grid[p] + res_p.value_grid[p]
            assert math.isclose(c_n, expected_c_n, abs_tol=1e-9)

    expected_f0 = base_model.s0 - K / ((1 + base_model.r)**N)
    assert math.isclose(res_f.v0, expected_f0, abs_tol=1e-9)


def test_exercise_2_12_chooser_option(base_model):
    """
    Exercise 2.12: Evaluates a Chooser option at time m.
    Shows the time 0 price is Put(K, N) + Call(K / (1+r)^{N-m}, m)
    relying solely on martingale properties and engine combinations.
    """
    N = 3
    m = 1
    K = 5.0

    engine = PricingEngine()
    res_call_N = engine.price(base_model, EuropeanCall(strike=K), n_periods=N)
    res_put_N = engine.price(base_model, EuropeanPut(strike=K), n_periods=N)

    chooser_m = {}
    for seq in product("HT", repeat=m):
        path = "".join(seq)
        chooser_m[path] = max(res_call_N.value_grid[path], res_put_N.value_grid[path])

    p_tilde, _ = base_model.risk_neutral_prob
    space = CoinTossSpace(n_periods=m, p=p_tilde)
    chooser_0 = space.expectation(chooser_m) / ((1 + base_model.r)**m)

    adjusted_strike = K / ((1 + base_model.r)**(N - m))
    price_put_N = res_put_N.v0
    price_call_m = engine.price(base_model, EuropeanCall(strike=adjusted_strike), n_periods=m).v0

    assert math.isclose(chooser_0, price_put_N + price_call_m, abs_tol=1e-9)

def test_exercise_2_7_martingale_not_markov():
    """
    Exercise 2.7: A stochastic process that is a martingale but not Markov.
    Constructs a custom M_n where reaching the exact same state (M_2 = 0) 
    via two different paths (HH vs TH) leads to two strictly different 
    future probability distributions for M_3, destroying the Markov property.
    """
    space = CoinTossSpace(n_periods=3, p=0.5)
    process = [
        {"": 0.0},
        {"H": 1.0, "T": -1.0},
        {"HH": 0.0, "HT": 2.0, "TH": 0.0, "TT": -2.0},
        {
            "HHH": 1.0, "HHT": -1.0,
            "HTH": 2.0, "HTT": 2.0,
            "THH": 5.0, "THT": -5.0,
            "TTH": -2.0, "TTT": -2.0
        }
    ]
    
    assert is_martingale(space, process)
    assert not is_markov(space, process)

def test_exercise_2_13_asian_option_markov(base_model):
    """
    Exercise 2.13 (i): The two-dimensional process (S_n, Y_n) where Y_n = sum_{k=0}^n S_k
    is a valid K-dimensional Markov process.
    """
    N = 3
    p_tilde, _ = base_model.risk_neutral_prob
    space = CoinTossSpace(n_periods=N, p=p_tilde)
    
    process = []
    for n in range(N + 1):
        state_n = {}
        prefixes = [""] if n == 0 else ["".join(seq) for seq in product("HT", repeat=n)]
        for p in prefixes:
            prices = base_model.price_path(p)
            y_n = sum(prices)
            s_n = prices[-1]
            state_n[p] = (s_n, y_n)
        process.append(state_n)
        
    assert is_markov(space, process)

def test_exercise_2_14_delayed_asian_option_markov_and_pricing(base_model):
    """
    Exercise 2.14: Delayed Asian option pricing where Y_n sums S_k from M+1 to N.
    (i) Verifies the (S_n, Y_n) process is Markov under the risk-neutral measure.
    (ii) Validates state reduction engine against brute-force engine.
    """
    N = 3
    M = 1
    K = 4.0
    
    p_tilde, _ = base_model.risk_neutral_prob
    space = CoinTossSpace(n_periods=N, p=p_tilde)
    
    process = []
    for n in range(N + 1):
        state_n = {}
        prefixes = [""] if n == 0 else ["".join(seq) for seq in product("HT", repeat=n)]
        for p in prefixes:
            prices = base_model.price_path(p)
            if n <= M:
                y_n = 0.0
            else:
                y_n = sum(prices[M+1:n+1])
            s_n = prices[-1]
            state_n[p] = (s_n, y_n)
        process.append(state_n)
        
    assert is_markov(space, process)
    
    payoff = DelayedAsianOption(strike=K, n_periods=N, m_delay=M)
    res_brute = PricingEngine().price(base_model, payoff, n_periods=N)
    res_reduced = ReducedStateEngine().price(base_model, payoff, n_periods=N)
    
    assert res_reduced.v0 == pytest.approx(res_brute.v0)
    assert res_reduced.delta0 == pytest.approx(res_brute.delta0)

def test_example_3_1_2_lookback_option(base_model):
    """
    Example 3.1.2: Pricing a three-period lookback option via Change of Measure.
    Uses the model from Example 1.2.4 with actual probability p=2/3.
    """
    n_periods = 3
    actual_space = CoinTossSpace(n_periods=n_periods, p=2/3)
    rn_space = CoinTossSpace(n_periods=n_periods, p=0.5)

    z_dict = radon_nikodym_derivative(actual_space, rn_space)
    
    assert z_dict["HHH"] == pytest.approx(27/64)
    assert z_dict["HHT"] == pytest.approx(27/32)
    assert z_dict["HTH"] == pytest.approx(27/32)
    assert z_dict["HTT"] == pytest.approx(27/16)
    assert z_dict["THH"] == pytest.approx(27/32)
    assert z_dict["THT"] == pytest.approx(27/16)
    assert z_dict["TTH"] == pytest.approx(27/16)
    assert z_dict["TTT"] == pytest.approx(27/8)

    payoff = LookbackOption()
    payoff_dict = {
        w: payoff.compute(base_model.price_path(w))
        for w in actual_space.get_omega()
    }

    assert payoff_dict["HHH"] == pytest.approx(0.0)
    assert payoff_dict["HHT"] == pytest.approx(8.0)
    assert payoff_dict["HTT"] == pytest.approx(6.0)
    assert payoff_dict["TTT"] == pytest.approx(3.5)

    v0_rn = sum(
        payoff_dict[w] * rn_space.probability(w)
        for w in rn_space.get_omega()
    ) / ((1 + base_model.r) ** n_periods)
    assert v0_rn == pytest.approx(1.376)

    zeta_dict = state_price_density(actual_space, rn_space, base_model.r, n_periods)
    v0_state_prices = price_via_state_prices(payoff_dict, actual_space, zeta_dict)
    assert v0_state_prices == pytest.approx(1.376)

def test_exercise_3_4_asian_option(base_model):
    """
    Exercise 3.4 (i)-(ii): Explicitly compute state price densities and 
    use them to price the Asian option of Exercise 1.8.
    """
    n_periods = 3
    actual_space = CoinTossSpace(n_periods=n_periods, p=2/3)
    rn_space = CoinTossSpace(n_periods=n_periods, p=0.5)

    zeta_dict = state_price_density(actual_space, rn_space, base_model.r, n_periods)

    assert zeta_dict["HHH"] == pytest.approx(0.216)  
    
    assert zeta_dict["HHT"] == pytest.approx(0.432)  
    assert zeta_dict["HTH"] == pytest.approx(0.432)
    assert zeta_dict["THH"] == pytest.approx(0.432)
    
    assert zeta_dict["HTT"] == pytest.approx(0.864)  
    assert zeta_dict["THT"] == pytest.approx(0.864)
    assert zeta_dict["TTH"] == pytest.approx(0.864)
    
    assert zeta_dict["TTT"] == pytest.approx(1.728)  

    payoff = AsianOption(strike=4.0, n_periods=n_periods)
    payoff_dict = {
        w: payoff.compute(base_model.price_path(w))
        for w in actual_space.get_omega()
    }
    
    v0_asian = price_via_state_prices(payoff_dict, actual_space, zeta_dict)
    assert v0_asian == pytest.approx(1.216)

def test_example_3_2_3_radon_nikodym_process(base_model):
    """
    Example 3.2.3: Recomputes the Z_n process for the three-period model 
    of Example 3.1.2 with actual probability p=2/3.
    """
    n_periods = 3
    actual_space = CoinTossSpace(n_periods=n_periods, p=2/3)
    rn_space = CoinTossSpace(n_periods=n_periods, p=0.5)

    z_process = radon_nikodym_process(actual_space, rn_space)

    assert z_process[2]["HH"] == pytest.approx(9/16)
    assert z_process[2]["HT"] == pytest.approx(9/8)
    assert z_process[2]["TH"] == pytest.approx(9/8)
    assert z_process[2]["TT"] == pytest.approx(9/4)

    assert z_process[1]["H"] == pytest.approx(3/4)
    assert z_process[1]["T"] == pytest.approx(3/2)

    assert z_process[0][""] == pytest.approx(1.0)


def test_exercise_3_4_iii_iv_asian_option_state_prices(base_model):
    """
    Exercise 3.4 (iii)-(iv): Compute state price densities zeta_2 and use 
    the state-price pricing formula at n=2 to recover V_2(HT) and V_2(TH) for 
    the Exercise 1.8 Asian option.
    """
    n_periods = 3
    actual_space = CoinTossSpace(n_periods=n_periods, p=2/3)
    rn_space = CoinTossSpace(n_periods=n_periods, p=0.5)

    zeta_process = state_price_density_process(actual_space, rn_space, base_model.r)
    assert zeta_process[2]["HT"] == pytest.approx(zeta_process[2]["TH"])

    payoff = AsianOption(strike=4.0, n_periods=n_periods)
    payoff_dict = {
        w: payoff.compute(base_model.price_path(w))
        for w in actual_space.get_omega()
    }
    
    v_2 = price_step_via_state_density_process(payoff_dict, actual_space, zeta_process, 2)
    
    assert v_2["HT"] != pytest.approx(v_2["TH"])

    engine = ReducedStateEngine()
    res_reduced = engine.price(base_model, payoff, n_periods=n_periods)
    
    v_2_ht_reduced = res_reduced.value_grid[(2, 4.0, 16.0)]
    assert v_2["HT"] == pytest.approx(v_2_ht_reduced)
    
    v_2_th_reduced = res_reduced.value_grid[(2, 4.0, 10.0)]
    assert v_2["TH"] == pytest.approx(v_2_th_reduced)


def test_exercise_3_3_discounted_stock_martingale(base_model):
    """
    Exercise 3.3: Build M_n = E_n[S_3] for the model of Figure 3.1.1 with 
    the actual probabilities (p=2/3), and assert it is a martingale.
    """
    n_periods = 3
    actual_space = CoinTossSpace(n_periods=n_periods, p=2/3)
    
    s_3_dict = {w: base_model.price_path(w)[-1] for w in actual_space.get_omega()}
    
    m_process = [actual_space.conditional_expectation(s_3_dict, n) for n in range(n_periods + 1)]
    
    assert is_martingale(actual_space, m_process)


def test_example_3_3_2_log_utility():
    """
    Example 3.3.2: Two-period optimal investment under log utility.
    Cross-validates the general solver against hand-verified numeric values.
    """
    model = BinomialStockModel(s0=4.0, u=2.0, d=0.5, r=0.25)
    actual_space = CoinTossSpace(n_periods=2, p=2/3)
    utility = LogUtility()

    x_n_dict, result = solve_optimal_investment(model, actual_space, utility, x0=4.0)

    assert x_n_dict["HH"] == pytest.approx(100.0 / 9.0)
    assert x_n_dict["HT"] == pytest.approx(50.0 / 9.0)
    assert x_n_dict["TH"] == pytest.approx(50.0 / 9.0)
    assert x_n_dict["TT"] == pytest.approx(25.0 / 9.0)

    assert result.delta_grid[(0, 4.0)] == pytest.approx(5.0 / 9.0)
    assert result.delta_grid[(1, 8.0)] == pytest.approx(25.0 / 54.0)
    assert result.delta_grid[(1, 2.0)] == pytest.approx(25.0 / 27.0)

    assert result.value_grid[(1, 8.0)] == pytest.approx(20.0 / 3.0)
    assert result.value_grid[(1, 2.0)] == pytest.approx(10.0 / 3.0)


def test_exercise_3_6_log_utility_process():
    """
    Exercise 3.6: Verify X_n = X_0 / zeta_n at every step n for LogUtility.
    """
    model = BinomialStockModel(s0=4.0, u=2.0, d=0.5, r=0.25)
    actual_space = CoinTossSpace(n_periods=3, p=0.6)
    rn_space = CoinTossSpace(n_periods=3, p=0.5)

    utility = LogUtility()
    x0 = 5.0
    x_n_dict, result = solve_optimal_investment(model, actual_space, utility, x0=x0)

    zeta_process = state_price_density_process(actual_space, rn_space, model.r)

    for w in actual_space.get_omega():
        for n in range(4):
            prefix = w[:n]
            s_n = model.price_path(prefix)[-1]
            expected_x_n = x0 / zeta_process[n][prefix]
            assert result.value_grid[(n, s_n)] == pytest.approx(expected_x_n)


def test_exercise_3_7_power_utility_closed_form():
    """
    Exercise 3.7: Validate PowerUtility closed-form matches the 
    general Lagrangian approach (Eq. 3.3.26 via brentq numeric solver).
    """
    model = BinomialStockModel(s0=4.0, u=2.0, d=0.5, r=0.25)
    actual_space = CoinTossSpace(n_periods=3, p=0.6)

    utility_exact = PowerUtility(p=-1.0)
    x_n_exact, _ = solve_optimal_investment(model, actual_space, utility_exact, x0=10.0)

    class GenericPowerUtility(PowerUtility):
        def get_closed_form_lambda(self, x0, actual_space, z_dict, r):
            return None
            
    utility_numeric = GenericPowerUtility(p=-1.0)
    x_n_numeric, _ = solve_optimal_investment(model, actual_space, utility_numeric, x0=10.0)

    for w in actual_space.get_omega():
        assert x_n_exact[w] == pytest.approx(x_n_numeric[w])


def test_exercise_3_9_goal_probability():
    """
    Exercise 3.9: Maximizing probability of reaching goal.
    Assert X_N*(w) = gamma for the cheapest paths.
    """
    actual_space = CoinTossSpace(n_periods=2, p=2/3)
    rn_space = CoinTossSpace(n_periods=2, p=0.5)

    x_n_dict = solve_goal_probability_maximization(
        actual_space, rn_space, r=0.25, x0=3.2, gamma=10.0
    )

    values = list(x_n_dict.values())
    assert values.count(10.0) == 2
    assert values.count(0.0) == 2

def test_example_4_2_1_american_put():
    """
    Example 4.2.1: Two-period American put, strike 5, S0=4, u=2, d=0.5, r=0.25.
    v2(16)=0, v2(4)=1, v2(1)=4.
    v1(8)=0.40, v1(2)=3 (early exercise here).
    v0(4)=1.36, delta0 ~ -0.4333.
    Consumption at (1, 2) is 1.0.
    """
    model = BinomialStockModel(s0=4.0, u=2.0, d=0.5, r=0.25)
    payoff = EuropeanPut(strike=5.0)  
    
    engine = AmericanEngine()
    res = engine.price(model, payoff, n_periods=2)
    
    assert res.value_grid[(2, 16.0)] == pytest.approx(0.0)
    assert res.value_grid[(2, 4.0)] == pytest.approx(1.0)
    assert res.value_grid[(2, 1.0)] == pytest.approx(4.0)
    
    assert res.value_grid[(1, 8.0)] == pytest.approx(0.40)
    assert res.value_grid[(1, 2.0)] == pytest.approx(3.0)
    
    assert res.value_grid[(0, 4.0)] == pytest.approx(1.36)
    assert res.delta0 == pytest.approx(-13.0 / 30.0, rel=1e-3)
    
    assert res.consumption_grid[(1, 2.0)] == pytest.approx(1.0)


def test_exercise_4_1_put_call_straddle():
    """
    Exercise 4.1: Compare American Straddle with sum of American Call + Put.
    S0=4, u=2, d=0.5, r=0.25, N=3.
    V0^S < V0^P + V0^C
    """
    model = BinomialStockModel(s0=4.0, u=2.0, d=0.5, r=0.25)
    
    class StraddlePayoff(Payoff):
        def __init__(self, strike: float):
            self.strike = strike
        def compute(self, path: np.ndarray) -> float:
            return max(self.strike - path[-1], 0.0) + max(path[-1] - self.strike, 0.0)
    
    engine = AmericanEngine()
    
    v0_put = engine.price(model, EuropeanPut(strike=4.0), n_periods=3).v0
    v0_call = engine.price(model, EuropeanCall(strike=4.0), n_periods=3).v0
    v0_straddle = engine.price(model, StraddlePayoff(strike=4.0), n_periods=3).v0
    
    assert v0_straddle < v0_put + v0_call

def test_example_4_2_1_stopped_processes(base_model):
    """
    Example 4.2.1 continued (p. 97-100).
    Evaluates stopping the discounted stock price M_n and the discounted 
    American put price Y_n at stopping time tau and non-stopping time rho.
    """
    p_tilde, _ = base_model.risk_neutral_prob
    space = CoinTossSpace(n_periods=2, p=p_tilde)
    
    tau = {"HH": float('inf'), "HT": 2.0, "TH": 1.0, "TT": 1.0}
    rho = {"HH": 0.0, "HT": 0.0, "TH": 1.0, "TT": 2.0}
    
    assert is_stopping_time(space, tau)
    assert not is_stopping_time(space, rho)
    
    M = []
    for n in range(3):
        level = {}
        prefixes = [""] if n == 0 else ["".join(seq) for seq in product("HT", repeat=n)]
        for p in prefixes:
            s_n = base_model.price_path(p)[-1]
            level[p] = ((4.0/5.0) ** n) * s_n
        M.append(level)
        
    assert is_martingale(space, M)
    
    M_tau = stop_process(M, tau)
    assert M_tau[1]["H"] == pytest.approx(6.40)
    assert M_tau[2]["TH"] == pytest.approx(1.60)
    assert M_tau[2]["TT"] == pytest.approx(1.60)
    assert is_martingale(space, M_tau)
    
    M_rho = stop_process(M, rho)
    assert not is_martingale(space, M_rho)
    
    engine = AmericanEngine()
    res = engine.price(base_model, EuropeanPut(strike=5.0), n_periods=2)
    
    Y = []
    for n in range(3):
        level = {}
        prefixes = [""] if n == 0 else ["".join(seq) for seq in product("HT", repeat=n)]
        for p in prefixes:
            s_n = base_model.price_path(p)[-1]
            v = res.value_grid[(n, s_n)]
            level[p] = ((4.0/5.0) ** n) * v
        Y.append(level)
        
    assert is_supermartingale(space, Y)
    assert not is_martingale(space, Y)
    
    Y_tau = stop_process(Y, tau)
    assert Y_tau[2]["HH"] == pytest.approx(0.0)
    assert Y_tau[2]["HT"] == pytest.approx(0.64)
    assert Y_tau[2]["TH"] == pytest.approx(2.40)
    assert Y_tau[2]["TT"] == pytest.approx(2.40)
    assert is_martingale(space, Y_tau)

def test_exercise_4_4_insider_payoff():
    """
    Exercise 4.4: Insider payoff under rho has a higher risk-neutral expectation (1.74)
    than the standard American put price (1.36).
    """
    space = CoinTossSpace(n_periods=2, p=0.5)
    
    rho = {"HH": 0.0, "HT": 0.0, "TH": 1.0, "TT": 2.0}
    Y_payoff = {"HH": 1.0, "HT": 1.0, "TH": 3.0, "TT": 4.0}
    
    expected_val = 0.0
    for w in space.get_omega():
        prob = space.probability(w)
        discount = (4.0/5.0) ** rho[w]
        expected_val += prob * discount * Y_payoff[w]
        
    assert expected_val == pytest.approx(1.74)
    assert expected_val > 1.36

def test_example_4_2_1_continued_via_definition(base_model):
    """
    Example 4.2.1 continued. Evaluates Eq. (4.4.3), (4.4.4), and (4.4.5) explicitly 
    by listing the limited set of available stopping times in each sub-branch 
    to confirm the definitional maximum matches the recursive algorithm.
    """
    discount = 1.0 / (1.0 + base_model.r)
    
    v1_h = max(0.0, discount * 0.5, discount * 0.5)
    assert v1_h == pytest.approx(0.40)
    
    v1_t = max(3.0, 2.0)
    assert v1_t == pytest.approx(3.0)
    
    v0 = max(1.0, discount * (0.5 * v1_h + 0.5 * v1_t))
    assert v0 == pytest.approx(1.36)

def test_exercise_4_5_stopping_time_enumeration(base_model):
    """
    Exercise 4.5: Exhaustive enumeration of all 26 stopping times in S_0 
    for the two-period model. The maximal expected discounted payoff must 
    yield 1.36 and correspond exactly to the optimal stopping time in (4.4.6).
    """
    p_tilde, _ = base_model.risk_neutral_prob
    space = CoinTossSpace(n_periods=2, p=p_tilde)
    omega = space.get_omega()
    
    possible_times = [0, 1, 2, float('inf')]
    
    valid_taus = []
    for combo in product(possible_times, repeat=4):
        tau = dict(zip(omega, combo))
        if is_stopping_time(space, tau):
            valid_taus.append(tau)
            
    assert len(valid_taus) == 26
    
    max_expected_val = -1.0
    optimal_taus = []  
    
    for tau in valid_taus:
        expected_val = 0.0
        for w in omega:
            t = tau[w]
            if t <= 2:
                s_t = base_model.price_path(w[:int(t)])[-1]
                g_t = max(5.0 - s_t, 0.0)
                expected_val += space.probability(w) * ((1 / (1 + base_model.r))**t) * g_t
                
        if expected_val > max_expected_val + 1e-9:
            max_expected_val = expected_val
            optimal_taus = [tau]
        elif math.isclose(expected_val, max_expected_val, rel_tol=1e-9, abs_tol=1e-9):
            optimal_taus.append(tau)
            
    assert max_expected_val == pytest.approx(1.36)
    
    book_tau = {"HH": float('inf'), "HT": 2.0, "TH": 1.0, "TT": 1.0}
    assert book_tau in optimal_taus

def test_exercise_4_3_running_average_put(base_model):
    """
    Exercise 4.3: American put on the running average.
    Cross-validates AmericanEngine's path-dependent framework against a 
    pure brute-force DP algorithm applied explicitly over the tree of histories.
    """
    K = 4.0
    N = 3
    payoff = RunningAveragePut(strike=K)
    
    engine_v0 = AmericanEngine().price(base_model, payoff, n_periods=N).v0
    
    space = CoinTossSpace(n_periods=N, p=0.5)
    V = {}
    
    for w in space.get_omega():
        path = base_model.price_path(w)
        V[w] = max(K - sum(path) / (N + 1), 0.0)
        
    for n in range(N - 1, -1, -1):
        prefixes = [""] if n == 0 else ["".join(seq) for seq in product("HT", repeat=n)]
        V_new = {}
        for p in prefixes:
            cont = (1 / (1 + base_model.r)) * (0.5 * V[p+"H"] + 0.5 * V[p+"T"])
            path = base_model.price_path(p)
            intr = max(K - sum(path) / (n + 1), 0.0)
            V_new[p] = max(intr, cont)
        V = V_new
        
    brute_v0 = V[""]
    
    assert engine_v0 == pytest.approx(brute_v0)

def test_exercise_4_6_and_4_7_bounds(base_model):
    """
    Exercise 4.6 (ii) and (iii): Bounds on the American put.
    Validates V_0^{AP} <= V_0^{EC} + K - S_0 (4.8.4) and 
    V_0^{EC} - S_0 + K/(1+r)^N <= V_0^{AP} (4.8.5).
    """
    N = 3
    K = 5.0
    
    v0_ap = AmericanEngine().price(base_model, EuropeanPut(strike=K), n_periods=N).v0
    v0_ec = ReducedStateEngine().price(base_model, EuropeanCall(strike=K), n_periods=N).v0
    
    assert v0_ap <= v0_ec + K - base_model.s0 + 1e-9
    
    lower_bound = v0_ec - base_model.s0 + K / ((1 + base_model.r) ** N)
    assert v0_ap >= lower_bound - 1e-9

def test_example_4_2_1_put_premium_vs_call(base_model):
    """
    Contrast motivating Theorem 4.5.1: In the model of Example 4.2.1 
    (S_0=4, u=2, d=0.5, r=0.25), an American put has a strict early exercise 
    premium, while an American call does not.
    """
    K = 5.0
    n_periods = 2
    
    put_payoff = EuropeanPut(strike=K)
    call_payoff = EuropeanCall(strike=K)
    
    am_engine = AmericanEngine()
    eu_engine = ReducedStateEngine()
    
    am_put_res = am_engine.price(base_model, put_payoff, n_periods)
    eu_put_res = eu_engine.price(base_model, put_payoff, n_periods)
    
    assert am_put_res.v0 == pytest.approx(1.36)
    assert am_put_res.v0 > eu_put_res.v0 + 1e-9
    
    assert any(c > 1e-9 for c in am_put_res.consumption_grid.values())
    
    am_call_res = am_engine.price(base_model, call_payoff, n_periods)
    eu_call_res = eu_engine.price(base_model, call_payoff, n_periods)
    
    assert am_call_res.v0 == pytest.approx(eu_call_res.v0)
    
    for c in am_call_res.consumption_grid.values():
        assert c == pytest.approx(0.0)

def test_page_126_explicit_tau_1_probabilities():
    """
    Explicit probabilities on page 126 for reaching level 1:
    P{tau_1 = 1} = 1/2
    P{tau_1 = 3} = 1/8
    P{tau_1 = 5} = 1/16
    
    Verified via closed-form formula (Route 1) AND brute-force counting over Omega (Route 2).
    """
    p_1 = first_passage_time_distribution(j=1, p=0.5)  # tau_1 = 1 => 2j-1 = 1 => j = 1
    p_3 = first_passage_time_distribution(j=2, p=0.5)  # tau_1 = 3 => 2j-1 = 3 => j = 2
    p_5 = first_passage_time_distribution(j=3, p=0.5)  # tau_1 = 5 => 2j-1 = 5 => j = 3
    
    assert p_1 == pytest.approx(1/2)
    assert p_3 == pytest.approx(1/8)
    assert p_5 == pytest.approx(1/16)
    
    space = CoinTossSpace(n_periods=5, p=0.5)
    count_1, count_3, count_5 = 0, 0, 0
    
    for w in space.get_omega():
        path = symmetric_random_walk_path(w)
        tau = first_passage_time(path, 1)
        if tau == 1:
            count_1 += 1
        elif tau == 3:
            count_3 += 1
        elif tau == 5:
            count_5 += 1
            
    prob_1 = count_1 / 32.0
    prob_3 = count_3 / 32.0
    prob_5 = count_5 / 32.0
    
    assert prob_1 == pytest.approx(1/2)
    assert prob_3 == pytest.approx(1/8)
    assert prob_5 == pytest.approx(1/16)

def test_exercise_5_1_multiplicative_property_mgf_for_american_put():
    """
    Exercise 5.1 / Eq. (5.7.1) evaluated at exact values m=2 and alpha=4/5.
    This serves as a preview to Section 5.4 (Perpetual American Put), where alpha = 1 / (1+r).
    
    Double-verifies the algorithmic evaluation against a manual paper-computed fraction.
    """
    m = 2
    alpha = 4.0 / 5.0
    
    val_m2 = first_passage_time_mgf(alpha, m)
    
    val_m1_squared = first_passage_time_mgf(alpha, 1) ** 2
    
    assert math.isclose(val_m2, val_m1_squared, abs_tol=1e-9)
    assert val_m2 == pytest.approx(1.0 / 4.0)