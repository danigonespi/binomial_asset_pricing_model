import numpy as np
from typing import Literal
from dataclasses import dataclass, field

from .equity_model import BinomialStockModel
from .payoffs import Payoff
from .engines import StateKey

@dataclass
class AmericanPricingResult:
    v0: float
    delta0: float
    value_grid: dict[StateKey, float] = field(default_factory=dict)
    delta_grid: dict[StateKey, float] = field(default_factory=dict)
    consumption_grid: dict[StateKey, float] = field(default_factory=dict)

class AmericanEngine:
    def price(self, model: BinomialStockModel, payoff: Payoff, n_periods: int,
              position: Literal["short", "long"] = "short") -> AmericanPricingResult:
        """
        Calculates the arbitrage-free price, the hedge, and the consumption process 
        for an American derivative using backward induction through state space reduction.

        Applies Eq. (4.2.5) for terminal values, Eq. (4.2.6) for the recursive
        risk-neutral value (including the early exercise premium),
        Eq. (4.2.7) for Delta, and Eq. (4.2.8) for the non-negative consumption.
        """
        value_grid = {}
        delta_grid = {}
        consumption_grid = {}
        
        p_tilde, q_tilde = model.risk_neutral_prob
        discount = 1.0 / (1.0 + model.r)

        u_powers = [1.0] * (n_periods + 2)
        d_powers = [1.0] * (n_periods + 2)
        for i in range(1, n_periods + 2):
            u_powers[i] = u_powers[i-1] * model.u
            d_powers[i] = d_powers[i-1] * model.d
            
        def get_s(j: int, n_step: int) -> float:
            return model.s0 * u_powers[j] * d_powers[n_step - j]

        states_by_level = {n: set() for n in range(n_periods + 1)}
        
        m0 = payoff.initial_aggregate(model.s0)
        states_by_level[0].add((0, m0)) 
        
        for n in range(n_periods):
            for j, m in states_by_level[n]:
                s_up = get_s(j + 1, n + 1)
                m_up = payoff.update_aggregate(m, s_up)
                states_by_level[n + 1].add((j + 1, m_up))
                
                s_down = get_s(j, n + 1)
                m_down = payoff.update_aggregate(m, s_down)
                states_by_level[n + 1].add((j, m_down))
                
        for j, m in states_by_level[n_periods]:
            s = get_s(j, n_periods)
            state_key = (n_periods, s) if m is None else (n_periods, s, m)
            
            g_s = payoff.terminal_value(s, m)
            v_N = max(g_s, 0.0)
            
            value_grid[state_key] = v_N
            consumption_grid[state_key] = 0.0
            
        for n in range(n_periods - 1, -1, -1):
            for j, m in states_by_level[n]:
                s = get_s(j, n)
                
                s_up = get_s(j + 1, n + 1)
                s_down = get_s(j, n + 1)
                
                m_up = payoff.update_aggregate(m, s_up)
                m_down = payoff.update_aggregate(m, s_down)
                
                key_up = (n+1, s_up) if m_up is None else (n+1, s_up, m_up)
                key_down = (n+1, s_down) if m_down is None else (n+1, s_down, m_down)
                
                cont_value = discount * (p_tilde * value_grid[key_up] + q_tilde * value_grid[key_down])
                g_s = payoff.terminal_value(s, m)
                
                v_n = max(g_s, cont_value)
                c_n = v_n - cont_value
                
                delta_n = (value_grid[key_up] - value_grid[key_down]) / (s_up - s_down)
                
                if position == "long":
                    delta_n = -delta_n
                    
                state_key = (n, s) if m is None else (n, s, m)
                value_grid[state_key] = v_n
                delta_grid[state_key] = delta_n
                consumption_grid[state_key] = c_n
                
        key0 = (0, model.s0) if m0 is None else (0, model.s0, m0)
        v0 = value_grid.get(key0, 0.0)
        delta0 = delta_grid.get(key0, 0.0)
        
        return AmericanPricingResult(
            v0=v0, 
            delta0=delta0, 
            value_grid=value_grid, 
            delta_grid=delta_grid,
            consumption_grid=consumption_grid
        )