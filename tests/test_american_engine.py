import pytest
import math
from itertools import product
from binomial_pricer.equity_model import BinomialStockModel
from binomial_pricer.payoffs import EuropeanPut, EuropeanCall
from binomial_pricer.engines import ReducedStateEngine
from binomial_pricer.american_engine import AmericanEngine
from binomial_pricer.probability_space import CoinTossSpace
from binomial_pricer.stochastic_properties import is_supermartingale

@pytest.fixture
def arbitrary_model():
    return BinomialStockModel(s0=10.0, u=1.2, d=0.9, r=0.05)

def test_american_value_greater_than_intrinsic(arbitrary_model):
    """Value grid must be >= max(g(s), 0) at all nodes."""
    payoff = EuropeanPut(strike=10.5)
    n_periods = 3
    engine = AmericanEngine()
    result = engine.price(arbitrary_model, payoff, n_periods)
    
    for state, v in result.value_grid.items():
        s = state[1]
        m = state[2] if len(state) > 2 else None
        g_s = payoff.terminal_value(s, m)
        assert v >= max(g_s, 0.0) - 1e-9

def test_consumption_is_nonnegative(arbitrary_model):
    """Consumption grid must be >= 0 at all nodes for any payoff."""
    payoff = EuropeanPut(strike=11.0)
    n_periods = 4
    engine = AmericanEngine()
    result = engine.price(arbitrary_model, payoff, n_periods)
    
    for c in result.consumption_grid.values():
        assert c >= -1e-9

def test_american_price_process_is_supermartingale(arbitrary_model):
    """The discounted American price process is a supermartingale under risk-neutral measure."""
    payoff = EuropeanPut(strike=10.5)
    n_periods = 3
    engine = AmericanEngine()
    result = engine.price(arbitrary_model, payoff, n_periods)
    
    p_tilde, _ = arbitrary_model.risk_neutral_prob
    space = CoinTossSpace(n_periods=n_periods, p=p_tilde)
    
    process = []
    for n in range(n_periods + 1):
        v_n_dict = {}
        prefixes = [""] if n == 0 else ["".join(seq) for seq in product("HT", repeat=n)]
        for p in prefixes:
            prices = arbitrary_model.price_path(p)
            s = prices[-1]
            m = payoff.initial_aggregate(arbitrary_model.s0)
            for step_s in prices[1:]:
                m = payoff.update_aggregate(m, step_s)
                
            target_state_key = None
            for key in result.value_grid.keys():
                if key[0] == n and math.isclose(key[1], s, rel_tol=1e-9):
                    key_m = key[2] if len(key) > 2 else None
                    if m is None and key_m is None:
                        target_state_key = key
                        break
                    elif m is not None and key_m is not None and math.isclose(key_m, m, rel_tol=1e-9):
                        target_state_key = key
                        break
            
            assert target_state_key is not None, f"State not found for n={n}, s={s}, m={m}"
            
            v = result.value_grid[target_state_key]
            v_n_dict[p] = v / ((1 + arbitrary_model.r) ** n)
        process.append(v_n_dict)
        
    assert is_supermartingale(space, process)

def test_deep_otm_american_matches_european(arbitrary_model):
    """For a derivative that is never optimal to exercise early, American == European, consumption == 0."""
    payoff = EuropeanCall(strike=100.0)
    n_periods = 3
    
    res_am = AmericanEngine().price(arbitrary_model, payoff, n_periods)
    res_eu = ReducedStateEngine().price(arbitrary_model, payoff, n_periods)
    
    assert res_am.v0 == pytest.approx(res_eu.v0)
    for state, c in res_am.consumption_grid.items():
        assert c == pytest.approx(0.0)

def test_american_engine_long_position_inverts_delta(arbitrary_model):
    payoff = EuropeanPut(strike=10.5)
    n_periods = 2
    
    res_short = AmericanEngine().price(arbitrary_model, payoff, n_periods, position="short")
    res_long = AmericanEngine().price(arbitrary_model, payoff, n_periods, position="long")
    
    for state, delta in res_short.delta_grid.items():
        assert res_long.delta_grid[state] == pytest.approx(-delta)