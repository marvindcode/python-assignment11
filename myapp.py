from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import plotly.data as pldata

df = pldata.stocks(return_type='pandas', indexed=False, datetimes=True)

app = Dash(__name__)

app.layout = html.Div([
    dcc.Dropdown(
        id="stock-dropdown",
        options=[{"label": symbol, "value": symbol} for symbol in df.columns],
        value="GOOG"
    ),
    dcc.Graph(id="stock-price")
])

@app.callback(
    Output("stock-price", "figure"),
    [Input("stock-dropdown", "value")]
)
def update_graph(symbol):
    fig = px.line(df, x="date", y=symbol, title=f"{symbol} Price")
    return fig

if __name__ == "__main__": 
    app.run(debug=True) 