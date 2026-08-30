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

def test_eq_2_3_7_and_2_3_8_boundary_conditions():
    """Eq (2.3.7): E_0[X] = EX, and Eq (2.3.8): E_N[X] = X"""
    space = CoinTossSpace(n_periods=2, p=0.4)
    X = {"HH": 1.0, "HT": 2.0, "TH": 3.0, "TT": 4.0}
    
    # E_0[X] -> n=0
    E0_X = space.conditional_expectation(X, 0)
    assert math.isclose(E0_X[""], space.expectation(X))
    
    # E_N[X] -> n=2
    EN_X = space.conditional_expectation(X, 2)
    assert EN_X == X

def test_theorem_2_3_2_i_linearity():
    """Theorem 2.3.2(i): Linearity of conditional expectations."""
    space = CoinTossSpace(n_periods=2, p=0.4)
    X = {"HH": 1.0, "HT": 2.0, "TH": 3.0, "TT": 4.0}
    Y = {"HH": 5.0, "HT": -1.0, "TH": 0.0, "TT": 2.0}
    c1, c2 = 2.0, -1.5
    
    combo = {w: c1 * X[w] + c2 * Y[w] for w in X}
    E_1_combo = space.conditional_expectation(combo, 1)
    
    E_1_X = space.conditional_expectation(X, 1)
    E_1_Y = space.conditional_expectation(Y, 1)
    
    for w in E_1_combo:
        expected = c1 * E_1_X[w] + c2 * E_1_Y[w]
        assert math.isclose(E_1_combo[w], expected)

def test_theorem_2_3_2_ii_taking_out_what_is_known():
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

def test_theorem_2_3_2_iii_iterated_conditioning():
    """Theorem 2.3.2(iii): E_n[E_m[X]] = E_n[X] for n <= m."""
    space = CoinTossSpace(n_periods=3, p=0.4)
    X = {"HHH": 1.0, "HHT": 2.0, "HTH": 3.0, "HTT": 4.0, 
         "THH": 5.0, "THT": 6.0, "TTH": 7.0, "TTT": 8.0}
    
    # E_2[X] has keys of length 2
    E_2_X = space.conditional_expectation(X, 2)
    # E_1[E_2[X]] resolves correctly because conditional_expectation uses the key length as 'm'
    E_1_E_2_X = space.conditional_expectation(E_2_X, 1)
    E_1_X = space.conditional_expectation(X, 1)
    
    for w in E_1_X:
        assert math.isclose(E_1_E_2_X[w], E_1_X[w])

def test_theorem_2_3_2_iv_independence():
    """Theorem 2.3.2(iv): E_n[X] = EX if X depends only on tosses n+1 to N."""
    space = CoinTossSpace(n_periods=2, p=0.6)
    # X depends ONLY on toss 2 (n+1 through N, where n=1).
    X = {"HH": 5.0, "HT": -2.0, "TH": 5.0, "TT": -2.0}
    
    E_1_X = space.conditional_expectation(X, 1)
    EX = space.expectation(X)
    
    for w in E_1_X:
        assert math.isclose(E_1_X[w], EX)

def test_theorem_2_3_2_v_conditional_jensen():
    """Theorem 2.3.2(v): Conditional Jensen's inequality E_n[phi(X)] >= phi(E_n[X])."""
    space = CoinTossSpace(n_periods=2, p=0.5)
    X = {"HH": 2.0, "HT": -1.0, "TH": 0.0, "TT": 4.0}
    
    # phi(x) = x^2 (convex)
    phi_X = {w: val**2 for w, val in X.items()}
    
    E_1_phi_X = space.conditional_expectation(phi_X, 1)
    E_1_X = space.conditional_expectation(X, 1)
    
    for w in E_1_X:
        assert E_1_phi_X[w] >= E_1_X[w]**2 - 1e-9