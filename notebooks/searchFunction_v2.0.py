# %%
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Output, Input, State
import dash_table as dt
import pickle
import pandas as pd
import flask
from waitress import serve


server = flask.Flask(__name__)
app = dash.Dash(__name__, server = server, url_base_pathname = '/polymers/')

@server.route('/')
def hello():
    """ Home Page """
    return 'Welcome to Digital Polymer Tool'

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
    """ Search results """
    
    if n_clicks and n_clicks > 0:
        filepath = 'grams_144_summary.pkl'
        with open(filepath,'rb') as f:
            search_word = pickle.load(f)
        
        try:
            rr = search_word[str(keyword)]
            df = pd.DataFrame(rr, columns = ('Source', 'Summary', 'Score'))
            df = df.sort_values('Score', ascending = False)
            return html.Div(['{} result(s) found for {}'.format(len(rr), str(keyword)), 
                             html.Br(), 
                             html.A(children = "Source Reports - Restricted", id = "link",
                             href = "https://my.shell.com/personal/ranja_sarkar_shell_com/_layouts/15/onedrive.aspx?id=%2Fpersonal%2Franja%5Fsarkar%5Fshell%5Fcom%2FDocuments%2FNon%2Dmetallic%20%28Polymer%29%20Reports%2Frestricted%20sources&FolderCTID=0x012000C9D15FB36E680F4E9B35A35F06C5CAAF"), 
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
    serve(app.server, host = "0.0.0.0") #default:8080

