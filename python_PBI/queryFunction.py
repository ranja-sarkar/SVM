# -*- coding: utf-8 -*-
"""
Created on Sun Dec 19 16:47:34 2021

@author: Ranja.Sarkar
"""


import sqlite3
import dash
import dash_html_components as html
#import dash_core_components as dcc
#from dash.dependencies import Output, Input, State
import dash_table as dt
import pandas as pd
#import flask
#import dash_bootstrap_components as dbc
#from waitress import serve

app = dash.Dash(__name__)
app.title = "Digital Polymer"

conn = sqlite3.connect('Polymer_Database.db')
tableName = 'DP_qual'
cursor = conn.cursor()

cursor.execute('SELECT * FROM {} limit 100'.format(tableName))

df = pd.read_sql("SELECT * FROM DP_qual limit 100",conn)

app = dash.Dash(__name__)

app.layout = html.Div([

    html.H1("This is a random table", style={'text-align': 'center'}),

    dt.DataTable(
    id = 'table',
    columns = [{"name": i, "id": i} for i in df.columns],
    data = df.to_dict('records'),
)])
    

if __name__ == "__main__":
    app.run_server(debug = True)
