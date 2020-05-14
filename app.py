# -*- coding: utf-8 -*-
"""
Created on Fri May 15 01:54:38 2020

@author: Ali
"""




    
    
import pandas as pd

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

df = pd.DataFrame()
df['Year']=(2011,2012,2013,2014,2015,2016,2017,2018,2019,2020)
df['polarity']=(122,175,225,180,110,157,268,305,400,305)
df['subjectivity']=(83,95,225,340,298,154,45,-25,0,35)

print(df.head())

x=df.Year

app = dash.Dash()

app.layout = html.Div(children=[
    html.Div(children='''
        Value to graph:
    '''),
    dcc.Dropdown(id='input',
                 options=[
                     {'label':'Polarity','value':'polarity'},
                     {'label':'Subjectivity','value':'subjectivity'}], value='polarity'),
        html.Div(id='output-graph'),

])

@app.callback(
    Output(component_id='output-graph', component_property='children'),
    [Input(component_id='input', component_property='value')]
)
def update_value(input_data):

    if input_data == 'subjectivity':
        y=df.subjectivity
    else :
        y=df.polarity


    return dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': x, 'y': y, 'type': 'line', 'name': input_data},
            ],
            'layout': {
                'title': input_data
            }
        }
    )

if __name__ == '__main__':
    app.run_server()

