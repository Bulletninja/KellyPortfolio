"""Sieves stocks based on Value Investing principles"""

import os
import sys
import time
import json
import datetime
import argparse
import numpy as np
import pandas as pd
import yfinance
from cvxopt import matrix
from cvxopt.solvers import qp
from sklearn.covariance import LedoitWolf
from typing import Dict

def get_good_deal_assets():
    """Gets the assets that are good deals based on the value investing principles"""

    assets = load_config('config.json') # dataframes of assets
    prices = load_prices(assets) # dataframes of prices
    
    # Gets the assets that are cheap based on the value investing principles
    peg_ratios = get_peg_ratios(prices, assets)
    good_deal_assets = peg_ratios[peg_ratios['PEG'] <= 1]
    return good_deal_assets


def get_peg_ratios(prices, assets):
    """Gets the PEG ratios for the assets"""

    # Gets the earnings per share
    eps = get_eps(prices, assets)

    # Gets the growth rates
    growth_rates = get_growth_rates(eps, assets)

    # Gets the PEG ratios
    peg_ratios = get_peg_ratios(growth_rates, assets)

    return peg_ratios