import pytest
from binomial_pricer.probability_space import CoinTossSpace
from binomial_pricer.stochastic_properties import is_martingale
from binomial_pricer.state_prices import (
    radon_nikodym_derivative,
    state_price_density,
    price_via_state_prices,
    radon_nikodym_process,
    state_price_density_process,
    price_step_via_state_density_process,
)


def test_z_is_strictly_positive_for_arbitrary_measures():
    """Theorem 3.1.1(i): Z(omega) > 0 for every omega, for any pair of equivalent measures."""
    actual = CoinTossSpace(n_periods=4, p=0.3)
    rn = CoinTossSpace(n_periods=4, p=0.7)
    z = radon_nikodym_derivative(actual, rn)
    assert all(val > 0 for val in z.values())


def test_expectation_of_z_under_actual_measure_is_one():
    """Theorem 3.1.1(ii): E[Z] = 1 under the actual measure, for arbitrary p, p_tilde, N."""
    actual = CoinTossSpace(n_periods=5, p=0.4)
    rn = CoinTossSpace(n_periods=5, p=0.6)
    z = radon_nikodym_derivative(actual, rn)
    e_z = sum(z[w] * actual.probability(w) for w in actual.get_omega())
    assert e_z == pytest.approx(1.0)


def test_change_of_measure_formula_for_arbitrary_random_variable():
    """Theorem 3.1.1(iii): E~[Y] = E[ZY], for an arbitrary Y unrelated to any option payoff."""
    n_periods = 3
    actual = CoinTossSpace(n_periods=n_periods, p=0.45)
    rn = CoinTossSpace(n_periods=n_periods, p=0.55)
    z = radon_nikodym_derivative(actual, rn)

    y = {w: sum(1.0 if c == 'H' else -1.0 for c in w) for w in actual.get_omega()}

    e_tilde_y = sum(y[w] * rn.probability(w) for w in rn.get_omega())
    e_zy = sum(z[w] * y[w] * actual.probability(w) for w in actual.get_omega())
    assert e_tilde_y == pytest.approx(e_zy)


def test_z_is_identically_one_when_measures_coincide():
    """If the actual and risk-neutral measures coincide, Z(omega) = 1 for every omega."""
    space = CoinTossSpace(n_periods=3, p=0.37)
    z = radon_nikodym_derivative(space, space)
    assert all(val == pytest.approx(1.0) for val in z.values())


def test_z_at_zero_periods_is_trivially_one():
    """Degenerate N=0 case: Omega = {''}, so Z('') = 1 regardless of p, p_tilde."""
    actual = CoinTossSpace(n_periods=0, p=0.2)
    rn = CoinTossSpace(n_periods=0, p=0.9)
    z = radon_nikodym_derivative(actual, rn)
    assert z[""] == pytest.approx(1.0)


def test_mismatched_n_periods_raises_value_error():
    with pytest.raises(ValueError):
        radon_nikodym_derivative(CoinTossSpace(3, 0.5), CoinTossSpace(2, 0.5))


def test_zeta_equals_z_discounted_for_arbitrary_model():
    """Eq. (3.1.9): zeta(omega) = Z(omega) / (1+r)^N, for arbitrary r and N."""
    n_periods, r = 4, 0.1
    actual = CoinTossSpace(n_periods=n_periods, p=0.35)
    rn = CoinTossSpace(n_periods=n_periods, p=0.65)
    z = radon_nikodym_derivative(actual, rn)
    zeta = state_price_density(actual, rn, r, n_periods)
    for w in actual.get_omega():
        assert zeta[w] == pytest.approx(z[w] / (1 + r) ** n_periods)


def test_passing_precomputed_z_dict_matches_recomputing_it():
    actual = CoinTossSpace(n_periods=3, p=0.4)
    rn = CoinTossSpace(n_periods=3, p=0.6)
    z = radon_nikodym_derivative(actual, rn)
    zeta_recomputed = state_price_density(actual, rn, r=0.2)
    zeta_reused = state_price_density(actual, rn, r=0.2, z_dict=z)
    assert zeta_recomputed == zeta_reused


def test_zeta_is_strictly_positive():
    actual = CoinTossSpace(n_periods=3, p=0.4)
    rn = CoinTossSpace(n_periods=3, p=0.6)
    zeta = state_price_density(actual, rn, r=0.1)
    assert all(val > 0 for val in zeta.values())


def test_pricing_a_sure_unit_payoff_gives_the_discount_factor():
    """
    A derivative paying 1 for certain at time N, regardless of path, must be
    priced at 1/(1+r)^N -- this follows directly from E[Z]=1 (Theorem 3.1.1(ii))
    and does not depend on any specific option payoff.
    """
    n_periods, r = 3, 0.25
    actual = CoinTossSpace(n_periods=n_periods, p=0.5)
    rn = CoinTossSpace(n_periods=n_periods, p=0.5)
    zeta = state_price_density(actual, rn, r, n_periods)
    sure_payoff = {w: 1.0 for w in actual.get_omega()}
    price = price_via_state_prices(sure_payoff, actual, zeta)
    assert price == pytest.approx(1 / (1 + r) ** n_periods)


def test_pricing_is_linear_in_the_payoff():
    """price_via_state_prices(aX + bY) = a*price(X) + b*price(Y), for arbitrary payoffs."""
    n_periods = 3
    actual = CoinTossSpace(n_periods=n_periods, p=0.3)
    rn = CoinTossSpace(n_periods=n_periods, p=0.7)
    zeta = state_price_density(actual, rn, r=0.05, n_periods=n_periods)

    x = {w: float(w.count('H')) for w in actual.get_omega()}
    y = {w: float(w.count('T')) for w in actual.get_omega()}
    a, b = 2.0, -3.0
    combo = {w: a * x[w] + b * y[w] for w in actual.get_omega()}

    price_combo = price_via_state_prices(combo, actual, zeta)
    price_x = price_via_state_prices(x, actual, zeta)
    price_y = price_via_state_prices(y, actual, zeta)
    assert price_combo == pytest.approx(a * price_x + b * price_y)


def test_terminal_value_of_process_equals_static_z():
    """Definition 3.2.4: Z_N = Z."""
    n_periods = 4
    actual = CoinTossSpace(n_periods=n_periods, p=0.4)
    rn = CoinTossSpace(n_periods=n_periods, p=0.6)
    z_static = radon_nikodym_derivative(actual, rn)
    z_process = radon_nikodym_process(actual, rn)
    assert z_process[n_periods] == pytest.approx(z_static)


def test_initial_value_of_process_is_one():
    """Definition 3.2.4: Z_0 = 1, for arbitrary p, p_tilde, N."""
    actual = CoinTossSpace(n_periods=4, p=0.15)
    rn = CoinTossSpace(n_periods=4, p=0.85)
    z_process = radon_nikodym_process(actual, rn)
    assert z_process[0][""] == pytest.approx(1.0)


def test_z_process_is_a_martingale_under_actual_measure():
    """Theorem 3.2.1: Z_n is a P-martingale, for an arbitrary (non-book) model."""
    actual = CoinTossSpace(n_periods=4, p=0.35)
    rn = CoinTossSpace(n_periods=4, p=0.8)
    z_process = radon_nikodym_process(actual, rn)
    assert is_martingale(actual, z_process)

    
def test_zeta_process_matches_definition_for_arbitrary_step():
    n_periods, r = 4, 0.1
    actual = CoinTossSpace(n_periods=n_periods, p=0.3)
    rn = CoinTossSpace(n_periods=n_periods, p=0.7)
    z_process = radon_nikodym_process(actual, rn)
    zeta_process = state_price_density_process(actual, rn, r)
    for n in range(n_periods + 1):
        for prefix, z_val in z_process[n].items():
            assert zeta_process[n][prefix] == pytest.approx(z_val / (1 + r) ** n)


def test_zeta_process_terminal_step_matches_static_state_price_density():
    n_periods, r = 3, 0.2
    actual = CoinTossSpace(n_periods=n_periods, p=0.45)
    rn = CoinTossSpace(n_periods=n_periods, p=0.55)
    zeta_static = state_price_density(actual, rn, r, n_periods)
    zeta_process = state_price_density_process(actual, rn, r)
    assert zeta_process[n_periods] == pytest.approx(zeta_static)


def test_price_at_maturity_equals_the_payoff_itself():
    n_periods = 3
    actual = CoinTossSpace(n_periods=n_periods, p=0.4)
    rn = CoinTossSpace(n_periods=n_periods, p=0.6)
    zeta_process = state_price_density_process(actual, rn, r=0.1)
    payoff = {w: float(w.count('H')) for w in actual.get_omega()}
    v_n = price_step_via_state_density_process(payoff, actual, zeta_process, n_periods)
    assert v_n == pytest.approx(payoff)


def test_price_at_time_zero_matches_the_static_state_price_formula():
    """
    Consistency between the two pricing routes given in the card: pricing at
    n=0 via the process-based formula (3.2.6) must match pricing directly via
    the static formula (3.1.10), for an arbitrary payoff and model.
    """
    n_periods = 3
    actual = CoinTossSpace(n_periods=n_periods, p=0.3)
    rn = CoinTossSpace(n_periods=n_periods, p=0.7)
    zeta_static = state_price_density(actual, rn, r=0.15, n_periods=n_periods)
    zeta_process = state_price_density_process(actual, rn, r=0.15)

    payoff = {w: float(w.count('H') - w.count('T')) ** 2 for w in actual.get_omega()}

    v0_static = price_via_state_prices(payoff, actual, zeta_static)
    v0_process = price_step_via_state_density_process(payoff, actual, zeta_process, 0)[""]
    assert v0_process == pytest.approx(v0_static)


def test_step_out_of_range_raises_value_error():
    n_periods = 3
    actual = CoinTossSpace(n_periods=n_periods, p=0.5)
    rn = CoinTossSpace(n_periods=n_periods, p=0.5)
    zeta_process = state_price_density_process(actual, rn, r=0.1)
    payoff = {w: 1.0 for w in actual.get_omega()}
    with pytest.raises(ValueError):
        price_step_via_state_density_process(payoff, actual, zeta_process, n_periods + 1)