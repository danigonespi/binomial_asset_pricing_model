import pytest
import math
from itertools import product
from binomial_pricer.probability_space import CoinTossSpace
from binomial_pricer.stochastic_properties import (
    is_martingale, 
    is_markov, 
    is_submartingale, 
    is_supermartingale
)

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
    
    # A true martingale satisfies both inequalities
    martingale = [{"": 0.0}, {"H": 1.0, "T": -1.0}, {"HH": 2.0, "HT": 0.0, "TH": 0.0, "TT": -2.0}]
    assert is_submartingale(space, martingale)
    assert is_supermartingale(space, martingale)

    # Submartingale (expected value grows)
    submartingale = [{"": 0.0}, {"H": 1.5, "T": -0.5}, {"HH": 3.0, "HT": 1.0, "TH": 1.0, "TT": -1.0}]
    assert is_submartingale(space, submartingale)
    assert not is_supermartingale(space, submartingale)

    # Supermartingale (expected value shrinks)
    supermartingale = [{"": 0.0}, {"H": 0.5, "T": -1.5}, {"HH": 1.0, "HT": -1.0, "TH": -1.0, "TT": -3.0}]
    assert is_supermartingale(space, supermartingale)
    assert not is_submartingale(space, supermartingale)


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
    assert not is_martingale(space, phi_M)  # Strictly convex functions destroy the pure equality


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