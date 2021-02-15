# Stock Portfolio Efficient Frontier Model

<p align="left">
    <a href="https://www.python.org/">
        <img src="https://ForTheBadge.com/images/badges/made-with-python.svg"
            alt="python"></a> &nbsp;
    <a href="https://opensource.org/licenses/MIT">
        <img src="https://img.shields.io/badge/License-MIT-brightgreen.svg?style=flat-square"
            alt="MIT license"></a> &nbsp;
</p>


The first them in this application is to import data. This is collected from Yahoo Finance's data using *pandas_datareader*. This model will only be using closing prices for the day.  

Maximizing Sharpe Ratio Portfolio
-------------
Since William Sharpe's creation of the Sharpe ratio in 1966 it has been one of the most referenced risk-return measures used in finance, and much of this popularity is attributed to its simplicity. Maximum Sharpe Portfolio or Tangency Portfolio is a portfolio on the efficient frontier at the point where line drawn from the point (0, risk-free rate) is tangent to the efficient frontier.
The expected return is first calculated on the inestment portfolio and then risk-free rate is subtracted from it. This is then dividided by the standard deviation of the portfolio. 


Efficient Frontier Model
-------------
The Efficient Frontier is a common phrase in Modern Finance since the inception of Modern Portfolio Theory in 1952 by Harry Markowitz. The efficient frontier is the set of optimal portfolios that offer the highest expected return for a defined level of risk or the lowest risk for a given level of expected return.



Package Dependencies
-------------

```python
pip install numpy
pip install pandas
pip install scipy
pip install pandas-datareader
pip install plotly
```
