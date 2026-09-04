import math
import pytest
from binomial_pricer.equity_model import BinomialStockModel
from binomial_pricer.probability_space import CoinTossSpace
from binomial_pricer.state_prices import radon_nikodym_derivative, state_price_density
from binomial_pricer.optimal_investment import (
    LogUtility,
    PowerUtility,
    GoalUtility,
    solve_optimal_investment,
    solve_goal_probability_maximization,
)


# --- Utility classes: internal mathematical consistency ---

def test_log_utility_inverse_marginal_undoes_marginal_utility():
    """I(U'(x)) = x for LogUtility, for arbitrary x > 0."""
    utility = LogUtility()
    for x in (0.5, 1.0, 3.7, 42.0):
        assert utility.inverse_marginal(utility.marginal_utility(x)) == pytest.approx(x)


def test_log_utility_marginal_matches_numerical_derivative():
    """U'(x) = 1/x should match a finite-difference approximation of U(x) = ln(x)."""
    utility = LogUtility()
    x, h = 2.0, 1e-6
    numerical_derivative = (utility.utility(x + h) - utility.utility(x - h)) / (2 * h)
    assert utility.marginal_utility(x) == pytest.approx(numerical_derivative, abs=1e-4)


def test_power_utility_rejects_invalid_parameters():
    with pytest.raises(ValueError):
        PowerUtility(p=1.0)
    with pytest.raises(ValueError):
        PowerUtility(p=0.0)
    with pytest.raises(ValueError):
        PowerUtility(p=1.5)


def test_power_utility_inverse_marginal_undoes_marginal_utility():
    """I(U'(x)) = x for PowerUtility, for arbitrary p < 1, p != 0, and x > 0."""
    for p in (-2.0, -0.5, 0.5):
        utility = PowerUtility(p=p)
        for x in (0.5, 1.0, 3.7, 42.0):
            assert utility.inverse_marginal(utility.marginal_utility(x)) == pytest.approx(x)


def test_power_utility_marginal_matches_numerical_derivative():
    utility = PowerUtility(p=-1.0)
    x, h = 2.0, 1e-6
    numerical_derivative = (utility.utility(x + h) - utility.utility(x - h)) / (2 * h)
    assert utility.marginal_utility(x) == pytest.approx(numerical_derivative, rel=1e-4)


def test_goal_utility_inverse_marginal_threshold_rule():
    """I(y) = gamma for 0 < y <= 1/gamma, and 0 for y > 1/gamma (Exercise 3.9(ii))."""
    utility = GoalUtility(gamma=10.0)
    assert utility.inverse_marginal(0.05) == pytest.approx(10.0)   # y = 1/gamma exactly
    assert utility.inverse_marginal(0.01) == pytest.approx(10.0)   # y < 1/gamma
    assert utility.inverse_marginal(0.2) == pytest.approx(0.0)     # y > 1/gamma


def test_goal_utility_marginal_utility_not_implemented():
    utility = GoalUtility(gamma=5.0)
    with pytest.raises(NotImplementedError):
        utility.marginal_utility(3.0)


# --- solve_optimal_investment: general properties, arbitrary models ---

def test_optimal_wealth_satisfies_the_budget_constraint():
    """
    Eq. (3.3.19)''/(3.3.26): E[zeta_N * X_N] = X_0 must hold for the solution,
    for an arbitrary model, actual measure, and utility -- not just Example 3.3.2.
    """
    model = BinomialStockModel(s0=10.0, u=1.5, d=0.6, r=0.1)
    actual_space = CoinTossSpace(n_periods=3, p=0.4)
    x0 = 7.0
    x_n_dict, _ = solve_optimal_investment(model, actual_space, LogUtility(), x0)

    rn_space = CoinTossSpace(n_periods=3, p=model.risk_neutral_prob[0])
    zeta = state_price_density(actual_space, rn_space, model.r, n_periods=3)

    budget = sum(zeta[w] * x_n_dict[w] * actual_space.probability(w) for w in actual_space.get_omega())
    assert budget == pytest.approx(x0)


def test_replicating_portfolio_starts_at_x0():
    """The portfolio constructed by Theorem 1.2.2 must start with initial wealth X_0."""
    model = BinomialStockModel(s0=10.0, u=1.5, d=0.6, r=0.1)
    actual_space = CoinTossSpace(n_periods=3, p=0.4)
    x0 = 7.0
    _, result = solve_optimal_investment(model, actual_space, LogUtility(), x0)
    assert result.v0 == pytest.approx(x0)


def test_first_order_condition_holds_across_all_paths():
    """
    Eq. (3.3.24): U'(X_N(omega)) = lambda * Z(omega)/(1+r)^N for the SAME
    lambda across every path -- verified by checking the ratio is constant.
    """
    model = BinomialStockModel(s0=10.0, u=1.5, d=0.6, r=0.1)
    actual_space = CoinTossSpace(n_periods=3, p=0.4)
    utility = PowerUtility(p=-0.5)
    x0 = 7.0
    x_n_dict, _ = solve_optimal_investment(model, actual_space, utility, x0)

    rn_space = CoinTossSpace(n_periods=3, p=model.risk_neutral_prob[0])
    z_dict = radon_nikodym_derivative(actual_space, rn_space)

    ratios = [
        utility.marginal_utility(x_n_dict[w]) / (z_dict[w] / (1 + model.r) ** 3)
        for w in actual_space.get_omega()
    ]
    assert all(ratio == pytest.approx(ratios[0]) for ratio in ratios)


def test_log_and_power_utility_agree_with_generic_numeric_solver():
    """
    For an arbitrary (non-book) model, the closed forms of Exercises 3.6/3.7
    must match what the generic brentq-based path in solve_optimal_investment
    finds when the closed form is disabled.
    """
    model = BinomialStockModel(s0=6.0, u=1.8, d=0.7, r=0.08)
    actual_space = CoinTossSpace(n_periods=3, p=0.55)
    x0 = 12.0

    class NumericLogUtility(LogUtility):
        def get_closed_form_lambda(self, x0, actual_space, z_dict, r):
            return None

    class NumericPowerUtility(PowerUtility):
        def get_closed_form_lambda(self, x0, actual_space, z_dict, r):
            return None

    cases = [
        (LogUtility(), NumericLogUtility()),
        (PowerUtility(p=-2.0), NumericPowerUtility(p=-2.0)),
    ]
    for closed_form_utility, numeric_utility in cases:
        x_closed, _ = solve_optimal_investment(model, actual_space, closed_form_utility, x0)
        x_numeric, _ = solve_optimal_investment(model, actual_space, numeric_utility, x0)
        for w in actual_space.get_omega():
            assert x_closed[w] == pytest.approx(x_numeric[w], rel=1e-6)


def test_log_utility_wealth_scales_linearly_with_x0():
    """X_n = X_0 / zeta_n (Exercise 3.6) is linear in X_0 -- doubling X_0 must double every X_n."""
    model = BinomialStockModel(s0=6.0, u=1.8, d=0.7, r=0.08)
    actual_space = CoinTossSpace(n_periods=3, p=0.55)

    x_n_small, _ = solve_optimal_investment(model, actual_space, LogUtility(), x0=4.0)
    x_n_large, _ = solve_optimal_investment(model, actual_space, LogUtility(), x0=8.0)

    for w in actual_space.get_omega():
        assert x_n_large[w] == pytest.approx(2.0 * x_n_small[w])


# --- solve_goal_probability_maximization: general properties ---

def test_goal_probability_wealth_is_always_zero_or_gamma():
    actual_space = CoinTossSpace(n_periods=3, p=0.4)
    rn_space = CoinTossSpace(n_periods=3, p=0.5)
    x_n_dict = solve_goal_probability_maximization(actual_space, rn_space, r=0.1, x0=2.0, gamma=5.0)
    assert all(v in (0.0, 5.0) for v in x_n_dict.values())


def test_goal_probability_respects_the_budget():
    """The actual-measure-discounted cost of the funded paths must not exceed X_0."""
    actual_space = CoinTossSpace(n_periods=3, p=0.4)
    rn_space = CoinTossSpace(n_periods=3, p=0.5)
    r, x0, gamma = 0.1, 2.0, 5.0
    x_n_dict = solve_goal_probability_maximization(actual_space, rn_space, r, x0, gamma)

    zeta = state_price_density(actual_space, rn_space, r, n_periods=3)
    cost = sum(zeta[w] * x_n_dict[w] * actual_space.probability(w) for w in actual_space.get_omega())
    assert cost <= x0 + 1e-6


def test_goal_probability_zero_budget_funds_nothing():
    actual_space = CoinTossSpace(n_periods=2, p=0.5)
    rn_space = CoinTossSpace(n_periods=2, p=0.5)
    x_n_dict = solve_goal_probability_maximization(actual_space, rn_space, r=0.1, x0=0.0, gamma=1.0)
    assert all(v == 0.0 for v in x_n_dict.values())


def test_goal_probability_ample_budget_funds_every_path():
    """If X_0 covers the cost of funding gamma on every single path, all paths get gamma."""
    actual_space = CoinTossSpace(n_periods=2, p=0.5)
    rn_space = CoinTossSpace(n_periods=2, p=0.5)
    r, gamma = 0.1, 1.0
    zeta = state_price_density(actual_space, rn_space, r, n_periods=2)
    total_cost = sum(zeta[w] * gamma * actual_space.probability(w) for w in actual_space.get_omega())

    x_n_dict = solve_goal_probability_maximization(actual_space, rn_space, r, x0=total_cost, gamma=gamma)
    assert all(v == pytest.approx(gamma) for v in x_n_dict.values())