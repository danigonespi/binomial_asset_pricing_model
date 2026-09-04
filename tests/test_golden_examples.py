import pytest
import math
from itertools import product
from binomial_pricer.equity_model import BinomialStockModel
from binomial_pricer.payoffs import EuropeanCall, LookbackOption, EuropeanPut, AsianOption, Forward, DelayedAsianOption
from binomial_pricer.engines import PricingEngine, ReducedStateEngine
from binomial_pricer.probability_space import CoinTossSpace
from binomial_pricer.stochastic_properties import is_martingale, is_markov
from binomial_pricer.state_prices import (
    radon_nikodym_derivative,
    state_price_density,
    price_via_state_prices,
    radon_nikodym_process,
    state_price_density_process,
    price_step_via_state_density_process,
)

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