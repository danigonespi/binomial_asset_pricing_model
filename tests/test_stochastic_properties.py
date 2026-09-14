import pytest
import math
from itertools import product
from binomial_pricer.probability_space import CoinTossSpace
from binomial_pricer.stochastic_properties import is_martingale, is_markov, is_submartingale, is_supermartingale, is_stopping_time, stop_process

def test_martingale_validation_rejects_wrong_length():
    space = CoinTossSpace(n_periods=3, p=0.5)
    with pytest.raises(ValueError, match="exactly N\\+1"):
        is_martingale(space, [{"": 1.0}])

def test_markov_validation_rejects_wrong_length():
    space = CoinTossSpace(n_periods=3, p=0.5)
    with pytest.raises(ValueError, match="exactly N\\+1"):
        is_markov(space, [{"": 1.0}])

def test_deterministic_process_is_trivially_markov():
    """A process that just grows deterministically is Markov."""
    space = CoinTossSpace(n_periods=2, p=0.5)
    process = [
        {"": 0.0},
        {"H": 1.0, "T": 1.0},
        {"HH": 2.0, "HT": 2.0, "TH": 2.0, "TT": 2.0},
    ]
    assert is_markov(space, process)


def test_submartingale_and_supermartingale_validation():
    space = CoinTossSpace(n_periods=2, p=0.5)
    
    martingale = [{"": 0.0}, {"H": 1.0, "T": -1.0}, {"HH": 2.0, "HT": 0.0, "TH": 0.0, "TT": -2.0}]
    assert is_submartingale(space, martingale)
    assert is_supermartingale(space, martingale)

    submartingale = [{"": 0.0}, {"H": 1.5, "T": -0.5}, {"HH": 3.0, "HT": 1.0, "TH": 1.0, "TT": -1.0}]
    assert is_submartingale(space, submartingale)
    assert not is_supermartingale(space, submartingale)

    supermartingale = [{"": 0.0}, {"H": 0.5, "T": -1.5}, {"HH": 1.0, "HT": -1.0, "TH": -1.0, "TT": -3.0}]
    assert is_supermartingale(space, supermartingale)
    assert not is_submartingale(space, supermartingale)

def test_constant_tau_is_stopping_time():
    """A rule that always stops at a fixed time k is a trivial stopping time."""
    space = CoinTossSpace(n_periods=3, p=0.5)
    for k in range(4):
        tau = {w: float(k) for w in space.get_omega()}
        assert is_stopping_time(space, tau)
        
def test_anticipating_tau_is_not_stopping_time():
    """A rule that looks ahead breaks the non-anticipating condition of Definition 4.3.1."""
    space = CoinTossSpace(n_periods=2, p=0.5)
    # At time 1, 'H' stops if the future is 'H' but continues if the future is 'T'.
    tau = {"HH": 1.0, "HT": 2.0, "TH": 0.0, "TT": 0.0}
    assert not is_stopping_time(space, tau)

def test_stopped_martingale_is_martingale():
    """Theorem 4.3.2 (Part I): A martingale stopped at a stopping time is a martingale."""
    space = CoinTossSpace(n_periods=3, p=0.5)
    
    process = []
    for n in range(4):
        level = {}
        prefixes = [""] if n == 0 else ["".join(seq) for seq in product("HT", repeat=n)]
        for p in prefixes:
            level[p] = sum(1.0 if c == 'H' else -1.0 for c in p)
        process.append(level)
        
    tau = {"HHH": 1.0, "HHT": 1.0, "HTH": 1.0, "HTT": 1.0, 
           "THH": 2.0, "THT": 2.0, "TTH": 3.0, "TTT": 3.0}
           
    assert is_stopping_time(space, tau)
    stopped = stop_process(process, tau)
    assert is_martingale(space, stopped)

def test_stopped_supermartingale_is_supermartingale():
    """Theorem 4.3.2 (Part I): A supermartingale stopped at a stopping time is a supermartingale."""
    space = CoinTossSpace(n_periods=2, p=0.5)
    
    process = [
        {"": 0.0},
        {"H": -1.0, "T": -3.0},
        {"HH": -2.0, "HT": -4.0, "TH": -4.0, "TT": -6.0}
    ]
    
    tau = {"HH": 1.0, "HT": 1.0, "TH": float('inf'), "TT": float('inf')}
    assert is_stopping_time(space, tau)
    
    stopped = stop_process(process, tau)
    assert is_supermartingale(space, stopped)