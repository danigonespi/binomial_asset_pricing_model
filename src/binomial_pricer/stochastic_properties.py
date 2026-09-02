import math
from typing import Any
from .probability_space import CoinTossSpace

def is_martingale(space: CoinTossSpace, process: list[dict[str, float]]) -> bool:
    """
    Verifies if an adapted stochastic process is a martingale.
    Uses Definition 2.4.1(i) and Eq. (2.4.2): M_n = E_n[M_{n+1}].
    """
    if len(process) != space.n_periods + 1:
        raise ValueError("The process must have exactly N+1 steps (from 0 to N).")

    for n in range(len(process) - 1):
        expected_next = space.conditional_expectation(process[n+1], n)
        current = process[n]
        
        for prefix in current:
            if not math.isclose(current[prefix], expected_next[prefix], rel_tol=1e-9, abs_tol=1e-9):
                return False
                
    return True

def is_submartingale(space: CoinTossSpace, process: list[dict[str, float]]) -> bool:
    """
    Verifies if an adapted stochastic process is a submartingale.
    Uses Definition 2.4.1(ii): M_n <= E_n[M_{n+1}].
    """
    if len(process) != space.n_periods + 1:
        raise ValueError("The process must have exactly N+1 steps (from 0 to N).")

    for n in range(len(process) - 1):
        expected_next = space.conditional_expectation(process[n+1], n)
        current = process[n]
        
        for prefix in current:
            if current[prefix] > expected_next[prefix] + 1e-9:
                return False
                
    return True

def is_supermartingale(space: CoinTossSpace, process: list[dict[str, float]]) -> bool:
    """
    Verifies if an adapted stochastic process is a supermartingale.
    Uses Definition 2.4.1(iii): M_n >= E_n[M_{n+1}].
    """
    if len(process) != space.n_periods + 1:
        raise ValueError("The process must have exactly N+1 steps (from 0 to N).")

    for n in range(len(process) - 1):
        expected_next = space.conditional_expectation(process[n+1], n)
        current = process[n]
        
        for prefix in current:
            if current[prefix] < expected_next[prefix] - 1e-9:
                return False
                
    return True

def _round_val(val: Any) -> Any:
    """Helper to handle float precision when grouping states (works for K-dimensions too)."""
    if isinstance(val, float):
        return round(val, 9)
    if isinstance(val, tuple):
        return tuple(round(v, 9) if isinstance(v, float) else v for v in val)
    return val

def is_markov(space: CoinTossSpace, process: list[dict[str, Any]]) -> bool:
    """
    Verifies if an adapted stochastic process is a Markov process (1D or K-Dimensional).
    Uses Definition 2.5.1 and Definition 2.5.5.
    
    A process is Markov if for any two paths that result in the same current state, 
    the conditional distribution of the next state is strictly identical, meaning 
    E_n[f(X_{n+1})] depends only on X_n, not on the path taken to get there.
    """
    if len(process) != space.n_periods + 1:
        raise ValueError("The process must have exactly N+1 steps (from 0 to N).")

    for n in range(len(process) - 1):
        current = process[n]
        next_state = process[n+1]

        value_groups: dict[Any, list[str]] = {}
        for prefix, val in current.items():
            val_rounded = _round_val(val)
            if val_rounded not in value_groups:
                value_groups[val_rounded] = []
            value_groups[val_rounded].append(prefix)

        for val, prefixes in value_groups.items():
            if len(prefixes) < 2:
                continue
                
            distributions = []
            for prefix in prefixes:
                val_h = _round_val(next_state[prefix + 'H'])
                val_t = _round_val(next_state[prefix + 'T'])
                
                dist: dict[Any, float] = {}
                dist[val_h] = dist.get(val_h, 0.0) + space.p
                dist[val_t] = dist.get(val_t, 0.0) + space.q
                distributions.append(dist)

            first_dist = distributions[0]
            for other_dist in distributions[1:]:
                if first_dist.keys() != other_dist.keys():
                    return False
                for k in first_dist:
                    if not math.isclose(first_dist[k], other_dist[k], rel_tol=1e-9, abs_tol=1e-9):
                        return False
                        
    return True