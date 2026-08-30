import pytest
import math
from itertools import product
from binomial_pricer.equity_model import BinomialStockModel
from binomial_pricer.payoffs import EuropeanCall, LookbackOption, EuropeanPut, AsianOption
from binomial_pricer.engines import PricingEngine, ReducedStateEngine
from binomial_pricer.probability_space import CoinTossSpace
from binomial_pricer.stochastic_properties import is_martingale, is_markov

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
    
    # Under risk-neutral (p=0.5), E[S_n] = S_0 * (1+r)^n. 
    # Here S0 = 4.0, r = 0.25 -> 1+r = 1.25
    assert math.isclose(rn_space.expectation(S1), 4.0 * 1.25)
    assert math.isclose(rn_space.expectation(S2), 4.0 * (1.25**2))
    assert math.isclose(rn_space.expectation(S3), 4.0 * (1.25**3))
    
    # Under actual (p=2/3), mean growth rate is pu + qd = (2/3)*2 + (1/3)*0.5 = 1.5
    act_space = CoinTossSpace(n_periods=3, p=2/3)
    assert math.isclose(act_space.expectation(S1), 4.0 * 1.5)
    assert math.isclose(act_space.expectation(S2), 4.0 * (1.5**2))
    assert math.isclose(act_space.expectation(S3), 4.0 * (1.5**3))

def test_exercise_2_4_random_walk_martingale():
    """Exercise 2.4: Symmetric random walk is a martingale."""
    space = CoinTossSpace(n_periods=3, p=0.5)
    
    # M_n = sum_{j=1}^n X_j where X_j = 1 if H else -1
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
    
    # Verifies Eq 2.3.2 algebraic identity
    assert math.isclose((p_tilde * base_model.u + q_tilde * base_model.d) / (1 + base_model.r), 1.0)
    
    # Verifies Eq 2.3.5 for n=1 -> S_1 = 1/(1+r) E_1[S_2]
    space = CoinTossSpace(n_periods=2, p=p_tilde)
    S_2 = {w: base_model.price_path(w)[-1] for w in space.get_omega()}
    
    E_1_S_2 = space.conditional_expectation(S_2, 1)
    
    for prefix in E_1_S_2:
        S_1 = base_model.price_path(prefix)[-1]
        assert math.isclose(S_1, (1 / (1 + base_model.r)) * E_1_S_2[prefix])