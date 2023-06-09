""" 
Estimates expected annual excess returns for a given asset from PEG ratios,
earnings per share, and growth rates using monte carlo simulation.
"""

def get_peg_ratios(growth_rates, assets):
    """Gets the PEG ratios for the assets"""

    # Gets the earnings per share
    eps = get_eps(prices, assets)

    # Gets the growth rates
    growth_rates = get_growth_rates(eps, assets)

    # Gets the PEG ratios
    peg_ratios = get_peg_ratios(growth_rates, assets)

    return peg_ratios

def get_excess_expected_returns(peg_ratios, assets):
    """Runs montecarlo to estimate distribution of expected returns"""
    pass


class EstimationsEngine:
    """ PEG, returns and growth estimators """
    pass