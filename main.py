import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import datetime as dt
from pandas_datareader import data as pdr


def getData(stocks, start, end):
    stocksData = pdr.get_data_yahoo(stocks, start=start, end=end)
    stocksData = stocksData["Close"]

    returns = stocksData.pct_change()
    meanReturns = returns.mean()
    covMatrix = returns.cov()

    return meanReturns, covMatrix


def portfolioPerformance(weights, meanReturns, covMatrix):
    returns = np.sum(meanReturns * weights) * 252
    stdDev = np.sqrt(np.dot(weights.T, np.dot(
        covMatrix, weights))) * np.sqrt(252)

    return returns, stdDev


def main():
    stocks = ['AAPL', 'ABBV', 'CSCO', 'O', 'T', 'VZ', 'XOM']

    endDate = dt.datetime.now()
    startDate = endDate - dt.timedelta(days=365)

    weights = np.array(
        [0.0782, 0.1020, 0.0828, 0.1149, 0.2270, 0.1877, 0.2075])

    meanReturns, covMatrix = getData(stocks, startDate, endDate)
    returns, stdDev = portfolioPerformance(weights, meanReturns, covMatrix)

    print(round(returns * 100, 2), round(stdDev * 100, 2))


if __name__ == '__main__':
    main()
