# -*- coding: utf-8 -*-
"""
@author: Ranja.Sarkar

#Running a Dash app within a Flask app

"""

#Libraries
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Output, Input, State
import dash_table as dt
import pickle
import pandas as pd
import flask

server = flask.Flask(__name__)

@server.route('/')
def hello():
    """ Home Page """
    return 'Welcome to Digital Polymer Search Tool'

app = dash.Dash(__name__, server = server, url_base_pathname = '/polymers/')

#App Design
colors = {'background': '#FFD500', 'text': '#ED1C24'}
app.layout = html.Div([
    html.H1('Search for non-metallics data', style = {'color': colors['text'], 'backgroundColor': colors['background']}),
    dcc.Input(placeholder = '', value = None, id = 'box', type = 'text', style = {'width': '25%'}),
    html.Button(id = 'button', children = 'Search', style = {'width': '5%'}),
    html.Hr(),
    html.Div(id = 'output')
                     ],

    style = {'textAlign': 'center', 'font-family': 'futura medium', 'font-size': '20px'}
                    )

@app.callback(Output('output', 'children'),
             [Input('button', 'n_clicks')],
             [State('box', 'value')])


@server.route("/polymers") 
def update_output(n_clicks, keyword):  
    """ Search result """
    
    if n_clicks and n_clicks > 0:
        filepath = 'grams_112_summary.pkl'
        with open(filepath,'rb') as f:
            search_word = pickle.load(f)
        
        try:
            rr = search_word[str(keyword)]
            df = pd.DataFrame(rr, columns = ('Source', 'Summary', 'Score', 'File'))
            df = df.sort_values('Score', ascending = False)
            return html.Div(['{} result(s) found for {}'.format(len(rr), str(keyword)),
            html.Br(), 
            html.Div(id = 'output_table'), dt.DataTable(id = 'table', data = df.to_dict('records'),
                columns = [{"name": i, "id": i} for i in df.columns], style_cell = {'textAlign': 'left', 'overflow': 'hidden', 'textOverflow': 'ellipsis', 'font-family': 'futura medium'}, style_data = {'whiteSpace': 'normal'}, style_header = 
                {'backgroundColor': '#FFD500', 'color': '#ED1C24', 'textAlign': 'center', 'font-family': 'futura medium'}, style_as_list_view = False)
                           ])
        except Exception:
            if len(keyword.split()) > 3:
                return html.Div([html.H4('Please restrict keyphrase to a maximum of 3 words')])
            else:
                return html.Div(['No result(s) found for {}'.format(str(keyword))])


if __name__ == "__main__":
    app.run_server(host = "localhost", port = 5001)
