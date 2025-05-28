from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import plotly.data as pldata
import pandas as pd

df = pldata.gapminder(return_type='pandas')

app = Dash(__name__)

server = app.server  

countries = pd.Series(df['country'].unique())

app.layout = html.Div([
    dcc.Dropdown(
        id='country-dropdown', 
        options=[{'label': country, 'value': country} for country in countries],
        value='Canada'  
    ),
    dcc.Graph(id='gdp-growth')  
])

@app.callback(
    Output('gdp-growth', 'figure'),
    [Input('country-dropdown', 'value')] 
)
def update_graph(country):
    filtered_df = df[df['country'] == country]
    
    fig = px.line(filtered_df, x='year', y='gdpPercap', title=f'{country} GDP Growth Over Time')
    
    return fig

if __name__ == '__main__':
    app.run(debug=True)
