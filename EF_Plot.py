import plotly.graph_objects as go
from CalculateResults import calculatedResults


# Plot min volitility, max sharpe ratio and effecient frontier
def EF_plot(meanReturns, covMatrix, riskFreeRate=0, constraintSet=(0, 1)):

    maxSR_returns, maxSR_stdDev, maxSR_allocation, minVol_returns, minVol_stdDev, minVol_allocation, effList, targetReturns = calculatedResults(
        meanReturns, covMatrix, riskFreeRate, constraintSet)

    # Max Sharpe Ratio
    MaxSharpeRatio = go.Scatter(
        name='Maximum Sharpe Ratio',
        mode='markers',
        x=[maxSR_stdDev],
        y=[maxSR_returns],
        marker=dict(color='red', size=14, line=dict(width=3, color='black'))
    )

    # Min Volitility
    MinVol = go.Scatter(
        name='Min Volitility',
        mode='markers',
        x=[minVol_stdDev],
        y=[minVol_returns],
        marker=dict(color='green', size=14, line=dict(width=3, color='black'))
    )

    # Efficient Frontier
    EF_curve = go.Scatter(
        name='Efficient Frontier',
        mode='lines',
        x=[round(ef_std * 100, 2) for ef_std in effList],
        y=[round(target * 100, 2) for target in targetReturns],
        line=dict(color='black', width=4, dash='dashdot')
    )

    data = [MaxSharpeRatio, MinVol, EF_curve]

    layout = go.Layout(
        title='Portfolio Optimisation with the Efficient Frontier',
        yaxis=dict(title='Annualised Return (%)'),
        xaxis=dict(title='Annualised Volatility (%)'),
        showlegend=True,
        legend=dict(
            x=0.75, y=0, traceorder='normal',
            bgcolor='#E2E2E2',
            bordercolor='black',
            borderwidth=2),
        width=800,
        height=600)

    fig = go.Figure(data=data, layout=layout)
    return fig.show()
