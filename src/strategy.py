# -*- coding: utf-8 -*-
from backtesting import Backtest, Strategy
from backtesting.lib import crossover

from backtesting.test import SMA, GOOG

# https://kernc.github.io/backtesting.py/doc/examples/Strategies%20Library.html


class Funding(Strategy):
    def init(self):
        pass

    def next(self):
        pass
    
    def generate_name():
        return "Strategy Name"

    def generate_description():
        return "Make Money"

    def generate_parameters():
        """
        Steps:
            1. Load the prices for the stocks
            2. Preprocess the data used in the strategy
            3. Combine the indicators into a single dataframe and add the strategy
            3. Create the backtest class and run the backtest
            4. Save the results into a pdf file in the output folder
        """
        return "Parameters"
    
    def generate_plot():
        # fileNameOutput=f"sandbox/output/{bt._strategy.__name__}.html"
        # bt.plot(filename=fileNameOutput)
        return "Plot"
    
    def generate_metrics():
        return "Metrics"
    
    def generate_pickle():
        return "Pickle"
    
    def generate_results():
        return "Results"
    
    def generate_report():
        # TODO: Generate a report
        return "Strategy Report"


# bt = Backtest(df, Funding,cash=25000, commission=.002, exclusive_orders=True)

# output = bt.run()
# output
