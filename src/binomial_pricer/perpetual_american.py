from typing import Callable
from .random_walk import first_passage_time_mgf

def exercise_policy_value(m: int, K: float = 4.0) -> float:
    """
    Calculates the value of the exercise policy tau_{-m} for a perpetual put.
    The policy exercises the first time the random walk falls m steps, which 
    corresponds to the stock price falling to S_0 * 2^{-m} (assuming S_0 = 4 
    as in the book's baseline setup for the passage time).
    
    Uses Eq. (5.4.2) and Eq. (5.4.3).
    """
    s_tau = 4.0 * (0.5 ** m)
    payoff = K - s_tau
    
    if payoff <= 0.0:
        return 0.0
        
    return payoff * first_passage_time_mgf(4.0 / 5.0, m)

def perpetual_put_boundary(K: float = 4.0) -> tuple[float, float]:
    """
    Calculates the optimal exercise boundary s_B and the constant B
    for the perpetual American put. Generalizes Exercise 5.9 (Eq. 5.7.7) 
    via the smooth pasting condition for an arbitrary strike K > 0.
    """
    if K <= 0:
        raise ValueError("Strike K must be strictly positive.")
        
    s_b = K / 2.0
    b = (K / 2.0) ** 2
    return s_b, b

def perpetual_put_value(s: float, K: float = 4.0) -> float:
    """
    Calculates the time-independent value v(s) of the perpetual American put.
    
    Uses Eq. (5.7.7), generalizing Eq. (5.4.11) for an arbitrary K.
    """
    if s <= 0:
        raise ValueError("Stock price s must be strictly positive.")
        
    s_b, b = perpetual_put_boundary(K)
    
    if s <= s_b:
        return K - s
    else:
        return b / s

def perpetual_put_consumption(s: float, K: float = 4.0) -> float:
    """
    Calculates the consumption c(s) for the hedging portfolio of the perpetual put.
    
    Uses Eq. (5.7.3), corrected for the missing 1/2 factor in the first term 
    present in the book's printed edition, ensuring mathematical consistency 
    with the symmetric Bellman continuation value of Eq. (5.4.12)/(5.4.13).
    """
    v_s = perpetual_put_value(s, K)
    v_up = perpetual_put_value(2.0 * s, K)
    v_down = perpetual_put_value(s / 2.0, K)
    
    return v_s - (4.0 / 5.0) * (0.5 * v_up + 0.5 * v_down)

def perpetual_put_delta(s: float, K: float = 4.0) -> float:
    """
    Calculates the position delta(s) in the stock for the hedging portfolio.
    
    Uses Eq. (5.7.4).
    """
    v_up = perpetual_put_value(2.0 * s, K)
    v_down = perpetual_put_value(s / 2.0, K)
    
    return (v_up - v_down) / (2.0 * s - s / 2.0)

def perpetual_call_value(s: float) -> float:
    """
    Calculates the time-independent value v(s) of the perpetual American call.
    
    Uses the result of Exercise 5.8(i), where v(s) = s.
    """
    if s <= 0:
        raise ValueError("Stock price s must be strictly positive.")
    return s

def bellman_residual(v_func: Callable[[float], float], g_func: Callable[[float], float], s: float, K: float = 4.0) -> float:
    """
    Calculates the residual of the general perpetual Bellman equation.
    Evaluates v_func(s) - max(g_func(s), 0.8 * [0.5 * v_func(2s) + 0.5 * v_func(s/2)]).
    
    Uses Eq. (5.4.16).
    """
    intrinsic = g_func(s)
    continuation = (4.0 / 5.0) * (0.5 * v_func(2.0 * s) + 0.5 * v_func(s / 2.0))
    
    return v_func(s) - max(intrinsic, continuation)