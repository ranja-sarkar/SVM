# -*- coding: utf-8 -*-

import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Output, Input, State
#from dash.exceptions import PreventUpdate
import dash_table as dt

import pickle
import pandas as pd
import flask

#external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
server = flask.Flask(__name__)
app = dash.Dash(__name__, server = server) #external stylesheet can be used here
#app.config.suppress_callback_exceptions = True

#@server.route('/hello')
#def hello():
#    return 'Hello World!'

#app = dash.Dash(__name__)
colors = {'background': '#FFD500', 'text': '#ED1C24'}

app.layout = html.Div([
    html.H1('Search for non-metallics data', style = {'color': colors['text'], 'backgroundColor': colors['background']}),
    dcc.Input(placeholder = '', value = None, id = 'box', type = 'text', style = {'width': '25%'}),
    html.Button(id = 'button', children = 'Search', style = {'width': '5%'}),
    html.Hr(),
    html.Div(id = 'output'),
    dcc.Link('Source Reports - Restricted', href = 'https://my.shell.com/personal/ranja_sarkar_shell_com/_layouts/15/onedrive.aspx?id=%2Fpersonal%2Franja%5Fsarkar%5Fshell%5Fcom%2FDocuments%2FNon%2Dmetallic%20%28Polymer%29%20Reports%2Frestricted%20sources'), 
    html.Br(),
    dcc.Link('Source Reports - Confidential', href = 'https://my.shell.com/personal/ranja_sarkar_shell_com/_layouts/15/onedrive.aspx?id=%2Fpersonal%2Franja%5Fsarkar%5Fshell%5Fcom%2FDocuments%2FNon%2Dmetallic%20%28Polymer%29%20Reports%2Fconfidential%20sources')
                    ],

#   style = {'columnCount': 1}
    style = {'textAlign': 'center', 'font-family': 'futura medium', 'font-size': '20px'}
                    )

@app.callback(Output('output', 'children'),
             [Input('button', 'n_clicks')],
             [State('box', 'value')])

def update_output(n_clicks, keyword):  
    
    if n_clicks > 0:
        filepath = 'C:/Users/Ranja.Sarkar/DPdatabase/failure_analysis_data/gramdic_116_summary.pkl'
        with open(filepath,'rb') as f:
            search_word = pickle.load(f)
        
        try:
            rr = search_word[str(keyword)]
            df = pd.DataFrame(rr, columns = ('Report', 'Relevance Score', 'Report Summary'))
            df = df.sort_values('Relevance Score', ascending = False)
            return html.Div([html.Div(id = 'output_table'), dt.DataTable(id = 'table', data = df.to_dict('records'),
                columns = [{"name": i, "id": i} for i in df.columns], style_cell = {'textAlign': 'left', 'overflow': 'hidden', 'textOverflow': 'ellipsis', 'font-family': 'futura medium'}, style_data = {'whiteSpace': 'normal'}, style_header = 
                {'backgroundColor': '#FFD500', 'color': '#ED1C24', 'textAlign': 'center', 'font-family': 'futura medium'}, style_as_list_view = False)
                        ])
        except Exception:
#            return (print(e)) ## works without n_clicks
            if len(keyword.split()) > 3:
                return html.Div([html.H6('Keyphrase not searchable')])
            else:
                return html.Div([html.H6('Keyword/keyphrase not found')])


if __name__ == "__main__":
#    from waitress import serve
#    serve(app.server, port = 2020)#    serve(app.server)
#    app.run_server(host = "localhost", port = 2020)
#    app.run_server()
    app.run_server()
    

