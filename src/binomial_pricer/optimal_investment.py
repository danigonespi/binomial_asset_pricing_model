import math
from abc import ABC, abstractmethod
from typing import Optional, Any
import numpy as np
from scipy.optimize import brentq

from .probability_space import CoinTossSpace
from .equity_model import BinomialStockModel
from .state_prices import radon_nikodym_derivative, state_price_density
from .payoffs import Payoff
from .engines import PricingResult, ReducedStateEngine

# Module-Level Architecture Note:
# Problem 3.3.1 optimally allocates terminal wealth by solving a static Lagrangian framework.
# For standard smooth utility functions (Logarithmic, Power), we use the generic
# `solve_optimal_investment` which inverts the marginal utility via Eq. (3.3.26).
# Conversely, Exercise 3.9 formulates a threshold/indicator goal utility. This
# function is not differentiable at the threshold, and its marginal inverse I(y)
# is a step function that necessitates sorting paths globally by state prices to
# greedily allocate budget. This breaks the generic single-path marginal inversion
# flow, so it is cleanly split into its own dedicated solver function:
# `solve_goal_probability_maximization`.

class Utility(ABC):
    @abstractmethod
    def utility(self, x: float) -> float:
        pass

    @abstractmethod
    def marginal_utility(self, x: float) -> float:
        pass

    @abstractmethod
    def inverse_marginal(self, y: float) -> float:
        """The functional inverse of U'(x), denoted as I(y)."""
        pass

    def get_closed_form_lambda(self, x0: float, actual_space: CoinTossSpace,
                               z_dict: dict[str, float], r: float) -> Optional[float]:
        """
        Returns the exact Lagrange multiplier lambda if a closed-form solution
        is known, avoiding numeric searches.
        """
        return None


class LogUtility(Utility):
    """
    Logarithmic utility U(x) = ln(x).
    Implements the closed-form solution described in Exercise 3.6.
    """
    def utility(self, x: float) -> float:
        return math.log(x) if x > 0 else -float('inf')

    def marginal_utility(self, x: float) -> float:
        return 1.0 / x

    def inverse_marginal(self, y: float) -> float:
        return 1.0 / y

    def get_closed_form_lambda(self, x0: float, actual_space: CoinTossSpace,
                               z_dict: dict[str, float], r: float) -> Optional[float]:
        """
        From Exercise 3.6: lambda = 1 / X_0.
        Derivation applies Eq. (3.3.26) directly to I(y) = 1/y.
        """
        return 1.0 / x0


class PowerUtility(Utility):
    """
    Power utility U_p(x) = (1/p) * x^p.
    Implements the closed-form solution described in Exercise 3.7.
    """
    def __init__(self, p: float):
        if p >= 1.0 or p == 0.0:
            raise ValueError("Parameter p must be < 1 and non-zero.")
        self.p = p

    def utility(self, x: float) -> float:
        if x <= 0:
            return -float('inf')
        return (1.0 / self.p) * (x ** self.p)

    def marginal_utility(self, x: float) -> float:
        return x ** (self.p - 1.0)

    def inverse_marginal(self, y: float) -> float:
        return y ** (1.0 / (self.p - 1.0))

    def get_closed_form_lambda(self, x0: float, actual_space: CoinTossSpace,
                               z_dict: dict[str, float], r: float) -> Optional[float]:
        """
        Extracts exact lambda directly from the structure of Exercise 3.7.
        """
        n = actual_space.n_periods
        exponent = self.p / (self.p - 1.0)
        e_z_pow = sum((z_dict[w] ** exponent) * actual_space.probability(w)
                      for w in actual_space.get_omega())
        base = x0 * ((1 + r) ** (n * exponent)) / e_z_pow
        return base ** (self.p - 1.0)


class GoalUtility(Utility):
    """
    Threshold rule utility for Exercise 3.9 (Kulldorff, Heath).
    U(x) = 1 if x >= gamma else 0.
    
    Note: The utility function is a step function and therefore not
    differentiable at the threshold gamma. It does not fit the generic
    marginal_utility continuous solver interface.
    """
    def __init__(self, gamma: float):
        self.gamma = gamma

    def utility(self, x: float) -> float:
        return 1.0 if x >= self.gamma else 0.0

    def marginal_utility(self, x: float) -> float:
        raise NotImplementedError("GoalUtility is not differentiable at the threshold.")

    def inverse_marginal(self, y: float) -> float:
        """
        Implements the exact piecewise rule from Exercise 3.9 (ii).
        I(y) = gamma if 0 < y <= 1/gamma, else 0.
        """
        return self.gamma if 0.0 < y <= (1.0 / self.gamma) else 0.0


class TerminalWealthPayoff(Payoff):
    """
    Locally defined Payoff to route the computed optimal terminal wealth
    X_N back through the standard backward induction engines.
    
    Justification for state-reduction capability: Since the terminal wealth
    X_N = I(lambda * Z / (1+r)^N) (Eq. 3.3.25) relies on the Radon-Nikodym
    derivative Z, and Z under Eq. (3.1.8) only depends on the sequence
    through the number of heads (equivalent to S_N), the optimal terminal
    wealth is solely a function of S_N.
    """
    def __init__(self, terminal_wealth_map: dict[str, float], model: BinomialStockModel):
        self.s_to_wealth = {}
        for w, x_n in terminal_wealth_map.items():
            s_final = model.price_path(w)[-1]
            s_key = round(s_final, 8)
            self.s_to_wealth[s_key] = x_n

    def compute(self, path: np.ndarray) -> float:
        return self.terminal_value(path[-1], None)

    def terminal_value(self, s_final: float, aggregate_final: Any) -> float:
        s_key = round(s_final, 8)
        return self.s_to_wealth[s_key]


def solve_optimal_investment(model: BinomialStockModel, actual_space: CoinTossSpace,
                             utility: Utility, x0: float) -> tuple[dict[str, float], PricingResult]:
    """
    Implements the complete algorithm from Theorem 3.3.6.
    Solves for the Lagrange multiplier lambda (via Eq. 3.3.26) and computes
    the optimal terminal wealth X_N (via Eq. 3.3.25). Then replicates it
    using standard backward induction.
    
    Note: As explicitly stated in the text, Equations (3.3.24)-(3.3.26)
    are printed using the plain terminal random variable Z rather than the
    Z_n or zeta_n notation. The variable names reflect this precisely.
    """
    n_periods = actual_space.n_periods
    rn_space = CoinTossSpace(n_periods=n_periods, p=model.risk_neutral_prob[0])
    z_dict = radon_nikodym_derivative(actual_space, rn_space)

    lam = utility.get_closed_form_lambda(x0, actual_space, z_dict, model.r)

    if lam is None:
        def budget_constraint(lam_guess: float) -> float:
            expected_val = 0.0
            for w in actual_space.get_omega():
                z = z_dict[w]
                discounted_z = z / ((1 + model.r) ** n_periods)
                expected_val += discounted_z * utility.inverse_marginal(lam_guess * discounted_z) * actual_space.probability(w)
            return expected_val - x0

        lam_low = 1e-6
        lam_high = 1.0
        while budget_constraint(lam_low) < 0:
            lam_low /= 10.0
        while budget_constraint(lam_high) > 0:
            lam_high *= 10.0
        lam = brentq(budget_constraint, lam_low, lam_high)

    x_n_dict = {}
    for w in actual_space.get_omega():
        z = z_dict[w]
        discounted_z = z / ((1 + model.r) ** n_periods)
        x_n_dict[w] = utility.inverse_marginal(lam * discounted_z)

    payoff = TerminalWealthPayoff(x_n_dict, model)
    engine = ReducedStateEngine()
    result = engine.price(model, payoff, n_periods=n_periods, position="short")

    return x_n_dict, result


def solve_goal_probability_maximization(actual_space: CoinTossSpace, rn_space: CoinTossSpace,
                                        r: float, x0: float, gamma: float) -> dict[str, float]:
    """
    Solves the probability maximization problem of Exercise 3.9.
    Selects paths ordered by ascending state price density zeta_m, allocating
    wealth gamma until the budget X_0 is exhausted.
    
    Implements Eq. (3.6.4) equivalently, mapping out X_N*(omega^m)
    as described in Eq. (3.6.5).
    """
    n_periods = actual_space.n_periods
    zeta_dict = state_price_density(actual_space, rn_space, r, n_periods)

    paths = actual_space.get_omega()
    paths_sorted = sorted(paths, key=lambda w: zeta_dict[w])

    x_n_dict = {w: 0.0 for w in paths}
    budget_used = 0.0

    for w in paths_sorted:
        cost_contribution = gamma * zeta_dict[w] * actual_space.probability(w)
        if budget_used + cost_contribution <= x0 + 1e-9:
            budget_used += cost_contribution
            x_n_dict[w] = gamma
        else:
            break

    return x_n_dict