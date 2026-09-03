import pytest
from binomial_pricer.equity_model import BinomialStockModel
from binomial_pricer.probability_space import CoinTossSpace
from binomial_pricer.payoffs import LookbackOption, AsianOption
from binomial_pricer.state_prices import (
    radon_nikodym_derivative,
    state_price_density,
    price_via_state_prices
)

def test_example_3_1_2_lookback_option(base_model):
    """
    Example 3.1.2: Pricing a three-period lookback option via Change of Measure.
    Uses the model from Example 1.2.4 with actual probability p=2/3.
    """
    n_periods = 3
    actual_space = CoinTossSpace(n_periods=n_periods, p=2/3)
    rn_space = CoinTossSpace(n_periods=n_periods, p=0.5)

    z_dict = radon_nikodym_derivative(actual_space, rn_space)
    
    assert z_dict["HHH"] == pytest.approx(27/64)
    assert z_dict["HHT"] == pytest.approx(27/32)
    assert z_dict["HTH"] == pytest.approx(27/32)
    assert z_dict["HTT"] == pytest.approx(27/16)
    assert z_dict["THH"] == pytest.approx(27/32)
    assert z_dict["THT"] == pytest.approx(27/16)
    assert z_dict["TTH"] == pytest.approx(27/16)
    assert z_dict["TTT"] == pytest.approx(27/8)

    payoff = LookbackOption()
    payoff_dict = {
        w: payoff.compute(base_model.price_path(w))
        for w in actual_space.get_omega()
    }

    assert payoff_dict["HHH"] == pytest.approx(0.0)
    assert payoff_dict["HHT"] == pytest.approx(8.0)
    assert payoff_dict["HTT"] == pytest.approx(6.0)
    assert payoff_dict["TTT"] == pytest.approx(3.5)

    v0_rn = sum(
        payoff_dict[w] * rn_space.probability(w)
        for w in rn_space.get_omega()
    ) / ((1 + base_model.r) ** n_periods)
    assert v0_rn == pytest.approx(1.376)

    zeta_dict = state_price_density(actual_space, rn_space, base_model.r, n_periods)
    v0_state_prices = price_via_state_prices(payoff_dict, actual_space, zeta_dict)
    assert v0_state_prices == pytest.approx(1.376)

def test_exercise_3_4_asian_option(base_model):
    """
    Exercise 3.4 (i)-(ii): Explicitly compute state price densities and 
    use them to price the Asian option of Exercise 1.8.
    """
    n_periods = 3
    actual_space = CoinTossSpace(n_periods=n_periods, p=2/3)
    rn_space = CoinTossSpace(n_periods=n_periods, p=0.5)

    zeta_dict = state_price_density(actual_space, rn_space, base_model.r, n_periods)

    assert zeta_dict["HHH"] == pytest.approx(0.216)  
    
    assert zeta_dict["HHT"] == pytest.approx(0.432)  
    assert zeta_dict["HTH"] == pytest.approx(0.432)
    assert zeta_dict["THH"] == pytest.approx(0.432)
    
    assert zeta_dict["HTT"] == pytest.approx(0.864)  
    assert zeta_dict["THT"] == pytest.approx(0.864)
    assert zeta_dict["TTH"] == pytest.approx(0.864)
    
    assert zeta_dict["TTT"] == pytest.approx(1.728)  

    payoff = AsianOption(strike=4.0, n_periods=n_periods)
    payoff_dict = {
        w: payoff.compute(base_model.price_path(w))
        for w in actual_space.get_omega()
    }
    
    v0_asian = price_via_state_prices(payoff_dict, actual_space, zeta_dict)
    assert v0_asian == pytest.approx(1.216)