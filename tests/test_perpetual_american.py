import pytest
import math
from binomial_pricer.equity_model import BinomialStockModel
from binomial_pricer.payoffs import EuropeanPut, EuropeanCall
from binomial_pricer.american_engine import AmericanEngine
from binomial_pricer.perpetual_american import perpetual_put_value, perpetual_call_value, perpetual_put_consumption, perpetual_put_delta, bellman_residual

def test_bellman_residual_put_generic():
    """
    Validates that the closed-form perpetual put value perfectly satisfies 
    the Bellman Eq. (5.4.16) across the exercise, boundary, and continuation regions 
    for an arbitrary generic strike.
    """
    K_generic = 6.0
    
    def v_func(s: float) -> float:
        return perpetual_put_value(s, K_generic)
        
    def g_func(s: float) -> float:
        return max(K_generic - s, 0.0)
        
    for j in range(-5, 6):
        s = K_generic * (2.0 ** j)
        residual = bellman_residual(v_func, g_func, s, K_generic)
        assert residual == pytest.approx(0.0, abs=1e-9)

def test_perpetual_put_boundary_conditions():
    """
    Validates the analytical limits as s -> 0 and s -> infinity.
    Uses Eq. (5.4.17).
    """
    K_generic = 7.5
    
    val_near_zero = perpetual_put_value(1e-9, K_generic)
    assert val_near_zero == pytest.approx(K_generic, abs=1e-6)
    
    val_near_inf = perpetual_put_value(1e9, K_generic)
    assert val_near_inf == pytest.approx(0.0, abs=1e-6)

def test_bellman_residual_call_generic():
    """
    Validates that the perpetual call satisfies the Bellman equation 
    and has no optimal exercise boundary (continuation always dominates intrinsic).
    Uses Exercise 5.8(i) and Eq. (5.4.16).
    """
    K_generic = 3.0
    
    def g_func(s: float) -> float:
        return max(s - K_generic, 0.0)
        
    for j in range(-5, 6):
        s = K_generic * (2.0 ** j)
        residual = bellman_residual(perpetual_call_value, g_func, s, K_generic)
        assert residual == pytest.approx(0.0, abs=1e-9)

def test_hedging_portfolio_replication():
    """
    Exercise 5.7(iii): Verifies that the hedging portfolio perfectly replicates 
    the perpetual derivative value at the next step regardless of up or down movements.
    This guarantees that the corrected consumption formula accurately reflects the arbitrage-free cost.
    """
    K_generic = 7.0
    r = 0.25
    
    for s in [2.0, 3.5, 7.0, 14.0]:
        v_s = perpetual_put_value(s, K_generic)
        c_s = perpetual_put_consumption(s, K_generic)
        delta_s = perpetual_put_delta(s, K_generic)
        
        cash_position = v_s - c_s - delta_s * s
        
        port_up = delta_s * (2.0 * s) + (1.0 + r) * cash_position
        v_up = perpetual_put_value(2.0 * s, K_generic)
        assert port_up == pytest.approx(v_up, abs=1e-9)
        
        port_down = delta_s * (s / 2.0) + (1.0 + r) * cash_position
        v_down = perpetual_put_value(s / 2.0, K_generic)
        assert port_down == pytest.approx(v_down, abs=1e-9)

def test_american_engine_convergence_to_perpetual_put():
    """
    Cross-validation between Chapter 4 (finite discrete backward induction) 
    and Chapter 5 (perpetual analytical formulas). 
    As the expiration N -> infinity, the time-zero finite American put value 
    must converge monotonically from below to the perpetual analytical value.
    """
    s0_generic = 6.0
    K_generic = 6.0
    
    model = BinomialStockModel(s0=s0_generic, u=2.0, d=0.5, r=0.25)
    payoff = EuropeanPut(strike=K_generic)
    engine = AmericanEngine()
    
    exact_perpetual_val = perpetual_put_value(s0_generic, K_generic)
    
    previous_val = -1.0
    for n_periods in [10, 20, 40, 80]:
        res = engine.price(model, payoff, n_periods)
        
        assert res.v0 > previous_val
        
        assert res.v0 <= exact_perpetual_val + 1e-9
        
        previous_val = res.v0
        
    assert previous_val == pytest.approx(exact_perpetual_val, abs=1e-4)

def test_american_engine_convergence_to_perpetual_call():
    """
    Cross-validation for the perpetual call. The finite horizon American call 
    never exercises early (per Theorem 4.5.1), and its value converges to S0.
    """
    s0_generic = 5.0
    K_generic = 6.0
    
    model = BinomialStockModel(s0=s0_generic, u=2.0, d=0.5, r=0.25)
    payoff = EuropeanCall(strike=K_generic)
    engine = AmericanEngine()
    
    exact_perpetual_val = perpetual_call_value(s0_generic)
    
    for n_periods in [10, 40, 80]:
        res = engine.price(model, payoff, n_periods)
        assert res.v0 <= exact_perpetual_val + 1e-9
        
    assert engine.price(model, payoff, 80).v0 == pytest.approx(exact_perpetual_val, abs=1e-4)