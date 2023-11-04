import dash
from dash import Dash, html, dcc
import dash_mantine_components as dmc
from callbacks_POC.callback_1 import *


app = Dash(__name__, use_pages=True)


def layout():
    return html.Div([
        html.H1('Multi-page app with Dash Pages'),
        html.Div([
            html.Div(
                dcc.Link(f"{page['name']} - {page['path']}", href=page["relative_path"])
            ) for page in dash.page_registry.values()
        ]),
        dash.page_container
    ])


app.layout = layout()


if __name__ == '__main__':
    app.run(debug=True, port=8090, host="0.0.0.0")

