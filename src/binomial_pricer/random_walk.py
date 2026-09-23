import math
import numpy as np
from .probability_space import CoinTossSpace

def symmetric_random_walk_path(coin_sequence: str) -> np.ndarray:
    """
    Generates the symmetric random walk path M_0, M_1, ..., M_n from a sequence of tosses.
    
    Uses Eq. (5.1.1) and Eq. (5.1.2).
    """
    path = [0.0]
    current = 0.0
    for coin in coin_sequence:
        if coin == 'H':
            current += 1.0
        elif coin == 'T':
            current -= 1.0
        else:
            raise ValueError(f"Unrecognized coin: {coin}")
        path.append(current)
    return np.array(path)

def first_passage_time(path: np.ndarray, m: int) -> int | float:
    """
    Calculates the first passage time tau_m, the first time the walk reaches level m.
    Returns math.inf if the walk never reaches m within the provided path.
    
    Uses Eq. (5.2.1).
    """
    if m == 0:
        raise ValueError("The level m must be a nonzero integer.")
        
    for n, val in enumerate(path):
        if math.isclose(val, m, rel_tol=1e-9, abs_tol=1e-9):
            return n
            
    return math.inf

def exponential_martingale_path(path: np.ndarray, sigma: float) -> np.ndarray:
    """
    Calculates the exponential martingale process S_n for a given random walk path.
    
    Uses Eq. (5.2.2).
    """
    if sigma <= 0:
        raise ValueError("sigma must be strictly positive (sigma > 0).")
        
    normalization = 2.0 / (math.exp(sigma) + math.exp(-sigma))
    s_n = []
    
    for n, m_n in enumerate(path):
        val = math.exp(sigma * m_n) * (normalization ** n)
        s_n.append(val)
        
    return np.array(s_n)

def first_passage_time_mgf(alpha: float, m: int) -> float:
    """
    Calculates the exact moment-generating function E[alpha^tau_m] for the 
    symmetric random walk reaching a nonzero integer level m.
    
    Uses Eq. (5.2.13).
    """
    if not (0.0 < alpha < 1.0):
        raise ValueError(f"Domain violation: alpha must be in (0, 1). Got {alpha}")
    if m == 0:
        raise ValueError("Domain violation: m must be a nonzero integer.")
        
    base = (1.0 - math.sqrt(1.0 - alpha**2)) / alpha
    return base ** abs(m)

def first_passage_time_distribution(j: int, p: float = 0.5) -> float:
    """
    Calculates the exact probability P{tau_1 = 2j - 1} that the first passage time 
    to level 1 occurs exactly at step 2j - 1, for a random walk with up-step probability p.
    
    Uses Eq. (5.2.23). When p = 0.5, this simplifies to Eq. (5.2.22).
    """
    if j < 1:
        raise ValueError("Domain violation: j must be a positive integer (j >= 1).")
    if not (0.0 < p < 1.0):
        raise ValueError("Domain violation: p must be in (0, 1).")
        
    q = 1.0 - p
    
    combinatorial_factor = math.factorial(2 * j - 2) / (math.factorial(j) * math.factorial(j - 1))
    
    return combinatorial_factor * (p ** j) * (q ** (j - 1))

def first_passage_time_distribution_via_reflection(j: int) -> float:
    """
    Calculates P{tau_1 = 2j - 1} for the symmetric random walk using the 
    purely combinatorial path reflection argument.
    
    Uses the unnumbered path-partition identity P{tau_1 <= 2j-1} = 1 - P{M_{2j-1} = -1}
    and differences it with the step prior to obtain the exact point probability (p. 128).
    """
    if j < 1:
        raise ValueError("Domain violation: j must be a positive integer (j >= 1).")
        
    def prob_tau_le(k: int) -> float:
        if k < 1:
            return 0.0
        # Evaluates P{tau_1 <= 2k-1} = 1 - P{M_{2k-1} = -1}
        # P{M_{2k-1} = -1} requires k-1 up-steps and k down-steps out of 2k-1 tosses.
        comb = math.factorial(2 * k - 1) / (math.factorial(k) * math.factorial(k - 1))
        return 1.0 - comb * (0.5 ** (2 * k - 1))
        
    return prob_tau_le(j) - prob_tau_le(j - 1)

def joint_distribution_walk_and_maximum(n: int, m: int, b: int) -> float:
    """
    Calculates P{M_n^* >= m, M_n = b} for a symmetric random walk.
    
    Uses the exact closed formula from Exercise 5.5(i), derived via 
    path reflection (p. 140).
    """
    if n <= 0 or n % 2 != 0:
        raise ValueError(f"Domain violation: n must be a positive even integer. Got {n}")
    if m <= 0 or m % 2 != 0:
        raise ValueError(f"Domain violation: m must be a positive even integer. Got {m}")
    if b % 2 != 0:
        raise ValueError(f"Domain violation: b must be an even integer. Got {b}")
    if b > m:
        raise ValueError(f"Domain violation: b ({b}) cannot be greater than m ({m}).")
    if m > n:
        raise ValueError(f"Domain violation: m ({m}) cannot exceed n ({n}).")
    if 2 * m - b > n:
        raise ValueError(f"Domain violation: 2m-b ({2 * m - b}) cannot exceed n ({n}).")
        
    n_minus = (n - b) // 2 + m
    n_plus = (n + b) // 2 - m
    
    combinatorial_factor = math.factorial(n) / (math.factorial(n_minus) * math.factorial(n_plus))
    return combinatorial_factor * (0.5 ** n)

def joint_distribution_walk_and_maximum_brute_force(n: int, m: int, b: int, p: float = 0.5) -> float:
    """
    Calculates P{M_n^* >= m, M_n = b} by explicitly enumerating all paths.
    Valid for any generic valid parameters n, m, b, and an arbitrary up-step 
    probability p.
    
    This addresses Exercise 5.5(ii) computationally without fabricating 
    a closed-form formula. Uses Eq. (5.7.2) definition of M_n^*.
    """
    if n <= 0:
        raise ValueError("n must be a positive integer.")
    if not (0.0 < p < 1.0):
        raise ValueError("Probability p must be in (0, 1).")
        
    space = CoinTossSpace(n_periods=n, p=p)
    prob_sum = 0.0
    
    for w in space.get_omega():
        path = symmetric_random_walk_path(w)
        m_n = path[-1]
        m_n_star = max(path[1:])
        
        if math.isclose(m_n, b, rel_tol=1e-9, abs_tol=1e-9) and m_n_star >= m - 1e-9:
            prob_sum += space.probability(w)
            
    return prob_sum