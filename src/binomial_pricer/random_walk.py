import math
import numpy as np

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