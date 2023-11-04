
from dash import html, dcc
from naming_conventions.InputContainer import InputName


def create_radio_item():

    return html.Div([
            "Select a city: ",
            dcc.RadioItems(
                options=['New York City', 'Montreal', 'San Francisco'],
                value='Montreal',
                id=InputName.input_1
            )
        ])


# Also, here can be created dataclasses for storing
# naming conventions about:
# - input component id,
# - input component property,
# - output component id,
# - output component property.




