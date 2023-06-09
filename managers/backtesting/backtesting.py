class BacktestingManager:
    """Manages backtesting"""
    
    def __init__(self, assets, start_date, end_date):
        self.assets = assets
        self.start_date = start_date
        self.end_date = end_date

    def backtest(self):
        """Backtests the assets"""
        pass