import datetime as dt
from pandas_datareader import data as pdr
from EF_Plot import EF_plot
from CalculateResults import calculatedResults


def getData(stocks, start, end):
    stocksData = pdr.get_data_yahoo(stocks, start=start, end=end)
    stocksData = stocksData["Close"]

    returns = stocksData.pct_change()
    meanReturns = returns.mean()
    covMatrix = returns.cov()

    return meanReturns, covMatrix


if __name__ == '__main__':
    stocks = ['AAPL', 'ABBV', 'CSCO', 'O', 'T', 'VZ', 'XOM']

    endDate = dt.datetime.now()
    startDate = endDate - dt.timedelta(days=365 * 10)

    meanReturns, covMatrix = getData(stocks, startDate, endDate)
    maxSR_returns, maxSR_stdDev, maxSR_allocation, minVol_returns, minVol_stdDev, minVol_allocation, effList, targetReturns = calculatedResults(
        meanReturns, covMatrix)

    print("Maximizing Sharpe Ratio Portfolio\n")
    print("Max Returns: ", maxSR_returns, " Max Standard Deviation: ",
          maxSR_stdDev, '\n', "Stock Allocation Recommendation\n",  maxSR_allocation)
    print("\nMinimum Volitility Portfolio\n")
    print("Max Returns: ", minVol_returns, " Max Standard Deviation: ",
          minVol_stdDev, '\n', "Stock Allocation Recommendation\n",  minVol_allocation)

    EF_plot(meanReturns, covMatrix)
