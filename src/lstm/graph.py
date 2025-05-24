import json
import plotly.graph_objs as go
import plotly


def graph(pred, actual, material_desc):
    predicted_sales_sc = go.Scatter(x=pred['date'], y=pred['sale_qty'], name='Predicted')
    actual_sales_sc = go.Scatter(x=actual['date'], y=actual['sale_qty'], name='Actual')
    layout = go.Layout(title=material_desc, xaxis=dict(title='Periode Penjualan'), yaxis=dict(title='Sale Quantity'))
    fig = go.Figure(data=[actual_sales_sc, predicted_sales_sc], layout=layout)
    fig = fig.update_yaxes(automargin=True)
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    return graphJSON