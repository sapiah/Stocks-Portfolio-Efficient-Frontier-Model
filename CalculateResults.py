import numpy as np
import pandas as pd
import scipy.optimize as sc


def portfolioPerformance(weights, meanReturns, covMatrix):
    returns = np.sum(meanReturns * weights) * 252
    stdDev = np.sqrt(np.dot(weights.T, np.dot(
        covMatrix, weights))) * np.sqrt(252)

    return returns, stdDev


def portfolioVariance(weights, meanReturns, covMatrix):
    return portfolioPerformance(weights, meanReturns, covMatrix)[1]


def portfolioReturn(weights, meanReturns, covMatrix):
    return portfolioPerformance(weights, meanReturns, covMatrix)[0]


def negativeSharpeRatio(weights, meanReturns, covMatrix, riskFreeRate=0):
    preturns, pstdDev = portfolioPerformance(weights, meanReturns, covMatrix)
    return -(preturns - riskFreeRate) / pstdDev

# Minimize the negative Sharpe Ratio by altering the weights of the portfolio


def maxSharpeRatio(meanReturns, covMatrix, riskFreeRate=0, constraintSet=(0, 1)):
    numAssets = len(meanReturns)
    args = (meanReturns, covMatrix, riskFreeRate)
    constraints = ({'type': 'eq', 'fun': lambda x: np.sum(x) - 1})
    bound = constraintSet
    bounds = tuple(bound for asset in range(numAssets))
    result = sc.minimize(negativeSharpeRatio, numAssets * [1. / numAssets], args=args,
                         method='SLSQP', bounds=bounds, constraints=constraints)
    return result


# Minimize the portfolio variance by altering the weights/allocation of assets in the portfolio
def minmizeVariance(meanReturns, covMatrix, constraintSet=(0, 1)):
    numAssets = len(meanReturns)
    args = (meanReturns, covMatrix)
    constraints = ({'type': 'eq', 'fun': lambda x: np.sum(x) - 1})
    bound = constraintSet
    bounds = tuple(bound for asset in range(numAssets))
    result = sc.minimize(portfolioVariance, numAssets * [1. / numAssets], args=args,
                         method='SLSQP', bounds=bounds, constraints=constraints)
    return result


# For each returnTarget, optimize portfolio for min variance
def effecientOpt(meanReturns, covMatrix, returnTarget, constraintSet=(0, 1)):
    numAssets = len(meanReturns)
    args = (meanReturns, covMatrix)

    constraints = ({'type': 'eq', 'fun': lambda x: portfolioReturn(
        x, meanReturns, covMatrix) - returnTarget}, {'type': 'eq', 'fun': lambda x: np.sum(x) - 1})
    bound = constraintSet
    bounds = tuple(bound for asset in range(numAssets))
    effOpt = sc.minimize(portfolioVariance, numAssets * [1. / numAssets], args=args,
                         method='SLSQP', bounds=bounds, constraints=constraints)

    return effOpt

# Gather financial information and output the max SR, min voliality, effecient frontier
def calculatedResults(meanReturns, covMatrix, riskFreeRate=0, constraintSet=(0, 1)):

    # Max Sharpe Ratio Portfolio
    maxSR_portfolio = maxSharpeRatio(meanReturns, covMatrix)
    maxSR_returns, maxSR_stdDev = portfolioPerformance(
        maxSR_portfolio['x'], meanReturns, covMatrix)

    maxSR_allocation = pd.DataFrame(
        maxSR_portfolio['x'], index=meanReturns.index, columns=['allocation'])
    maxSR_allocation.allocation = [
        round(i * 100, 0) for i in maxSR_allocation.allocation]

    # Min Volitility Portfolio
    minVol_portfolio = minmizeVariance(meanReturns, covMatrix)
    minVol_returns, minVol_stdDev = portfolioPerformance(
        minVol_portfolio['x'], meanReturns, covMatrix)

    minVol_allocation = pd.DataFrame(
        maxSR_portfolio['x'], index=meanReturns.index, columns=['allocation'])
    minVol_allocation.allocation = [
        round(i * 100, 0) for i in minVol_allocation.allocation]

    # Effecient Frontier
    effList = []
    targetReturns = np.linspace(minVol_returns, maxSR_returns, 20)
    for target in targetReturns:
        effList.append(effecientOpt(meanReturns, covMatrix, target)['fun'])

    maxSR_returns, maxSR_stdDev = round(
        maxSR_returns * 100, 2), round(maxSR_stdDev * 100, 2)
    minVol_returns, minVol_stdDev = round(
        minVol_returns * 100, 2), round(minVol_stdDev * 100, 2)

    return maxSR_returns, maxSR_stdDev, maxSR_allocation, minVol_returns, minVol_stdDev, minVol_allocation, effList, targetReturns
