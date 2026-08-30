import pytest
import math
from binomial_pricer.probability_space import CoinTossSpace

def test_eq_2_1_1_omega_generation():
    space = CoinTossSpace(n_periods=3, p=0.5)
    omega = space.get_omega()
    assert len(omega) == 8
    assert "HHH" in omega
    assert "TTT" in omega

def test_eq_2_1_4_probability_measure_sums_to_one():
    """Definition 2.1.1: Probabilities must sum to 1."""
    space = CoinTossSpace(n_periods=3, p=0.25)
    total_prob = sum(space.probability(w) for w in space.get_omega())
    assert math.isclose(total_prob, 1.0)

def test_eq_2_1_7_event_probability_and_complement():
    """Exercise 2.1: Event subsets and complement property."""
    space = CoinTossSpace(n_periods=2, p=0.4)
    event_A = {"HH", "HT"}  # First toss is Heads
    
    assert math.isclose(space.event_probability(event_A), 0.4)
    
    event_Ac = set(space.get_omega()) - event_A
    assert math.isclose(space.event_probability(event_Ac), 1.0 - space.event_probability(event_A))

def test_theorem_2_2_5_jensens_inequality():
    """Theorem 2.2.5: E[phi(X)] >= phi(E[X]) for a convex function."""
    space = CoinTossSpace(n_periods=2, p=0.5)
    X = {"HH": 2.0, "HT": -1.0, "TH": 0.0, "TT": 4.0}
    
    # phi(x) = x^2 is strictly convex
    phi_X = {w: val**2 for w, val in X.items()}
    
    E_phi_X = space.expectation(phi_X)
    phi_E_X = space.expectation(X) ** 2
    
    assert E_phi_X >= phi_E_X

def test_theorem_2_3_2_taking_out_what_is_known():
    """Theorem 2.3.2(ii): E_n[XY] = X E_n[Y] if X depends only on the first n tosses."""
    space = CoinTossSpace(n_periods=2, p=0.4)
    X = {"HH": 2.0, "HT": 2.0, "TH": 5.0, "TT": 5.0}  # Known at time 1
    Y = {"HH": 1.0, "HT": -1.0, "TH": 3.0, "TT": 4.0}
    
    XY = {w: X[w] * Y[w] for w in space.get_omega()}
    
    E_1_XY = space.conditional_expectation(XY, n=1)
    E_1_Y = space.conditional_expectation(Y, n=1)
    
    for prefix in ["H", "T"]:
        x_val = X[prefix + "H"]  # Constant for this prefix
        assert math.isclose(E_1_XY[prefix], x_val * E_1_Y[prefix])