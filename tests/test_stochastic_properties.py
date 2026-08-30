import pytest
from binomial_pricer.probability_space import CoinTossSpace
from binomial_pricer.stochastic_properties import is_martingale, is_markov

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