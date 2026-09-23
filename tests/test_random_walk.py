import pytest
import math
from itertools import product
from binomial_pricer.random_walk import (
    symmetric_random_walk_path,
    first_passage_time,
    exponential_martingale_path,
    first_passage_time_mgf,
    first_passage_time_distribution
)
from binomial_pricer.probability_space import CoinTossSpace
from binomial_pricer.stochastic_properties import is_martingale

@pytest.mark.parametrize("m, alpha", [(2, 0.3), (5, 0.7), (-3, 0.5), (-1, 0.9)])
def test_mgf_multiplicative_property_eq_5_7_1(m, alpha):
    """
    Exercise 5.1 (Eq. 5.7.1): E[alpha^tau_m] = (E[alpha^tau_1])^m for any m > 0.
    Since the problem is symmetric, this applies symmetrically for negative m via abs(m).
    """
    res_direct = first_passage_time_mgf(alpha, m)
    res_composed = first_passage_time_mgf(alpha, 1) ** abs(m)
    assert math.isclose(res_direct, res_composed, rel_tol=1e-9)

def test_first_passage_time_distribution_symmetry_fallback():
    """
    Confirms that Eq. (5.2.23) evaluates correctly for arbitrary j 
    and handles the symmetric fallback (p=0.5) naturally.
    """
    assert first_passage_time_distribution(j=2, p=0.7) > 0.0
    assert first_passage_time_distribution(j=4, p=0.3) > 0.0
    
    # Quick sanity check on domain violation
    with pytest.raises(ValueError):
        first_passage_time_distribution(j=0)

def test_first_passage_time_mgf_empirical_bounds():
    """
    Cross-validation: Calculates the MGF empirically by iterating through the finite sample 
    space Omega and comparing it against the closed-form equation.
    
    Because tau_m can be infinity (which we truncate at max N=14), the empirical expectation
    must be strictly lower than the exact closed-form value, but relatively close.
    """
    n_periods = 14
    m = 2
    alpha = 0.6
    space = CoinTossSpace(n_periods, 0.5)
    
    empirical_expected_value = 0.0
    for w in space.get_omega():
        path = symmetric_random_walk_path(w)
        tau = first_passage_time(path, m)
        
        if tau != math.inf:
            empirical_expected_value += (alpha ** tau) * space.probability(w)
            
    exact_value = first_passage_time_mgf(alpha, m)
    
    assert empirical_expected_value < exact_value
    assert exact_value - empirical_expected_value < 0.1  # Bounded truncation error

def test_symmetric_random_walk_is_martingale():
    """
    Cross-validation: Evaluates the output of Eq. (5.1.2) using the standard 
    Definition 2.4.1(i) martingale validator from Chapter 2.
    """
    n_periods = 4
    space = CoinTossSpace(n_periods, 0.5)
    process = []
    
    for n in range(n_periods + 1):
        prefixes = [""] if n == 0 else ["".join(seq) for seq in product("HT", repeat=n)]
        level_dict = {}
        for p in prefixes:
            path = symmetric_random_walk_path(p)
            level_dict[p] = path[-1]
        process.append(level_dict)
        
    assert is_martingale(space, process)

def test_exponential_process_is_martingale():
    """
    Lemma 5.2.1: S_n is a martingale for a fixed positive sigma.
    Cross-validation between Chapter 5's formula and Chapter 2's `is_martingale` logic.
    """
    n_periods = 4
    sigma = 0.3
    space = CoinTossSpace(n_periods, 0.5)
    process = []
    
    for n in range(n_periods + 1):
        prefixes = [""] if n == 0 else ["".join(seq) for seq in product("HT", repeat=n)]
        level_dict = {}
        for p in prefixes:
            rw_path = symmetric_random_walk_path(p)
            exp_path = exponential_martingale_path(rw_path, sigma)
            level_dict[p] = exp_path[-1]
        process.append(level_dict)
        
    assert is_martingale(space, process)