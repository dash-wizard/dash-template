

import dash
from dash import html, dcc, callback, Input, Output

from components.RadioItem import create_radio_item
from naming_conventions.OutputContainer import OutputDataClass, OutputTypeClass
from naming_conventions.InputContainer import InputName, InputType
from transformations.SimpleOutput import create_simple_output

from pydantic import validate_arguments


dash.register_page(__name__)


def layout():
    return html.Div([
        html.H1('This is our Analytics page'),

        create_radio_item(),

        html.Br(),
        html.Div(id=OutputDataClass.output_1),

        html.Div(id='1'),
        html.Div(id='2'),
        html.Div(id='3'),
        html.Div(id='4'),

    ])

#
# @callback(
#     # Output 0
#     Output(component_id=OutputDataClass.output_1, component_property=OutputTypeClass.children),
#
#     # Output 1
#     Output(component_id='1', component_property=OutputTypeClass.children),
#
#     # Output 2
#     Output(component_id='2', component_property=OutputTypeClass.children),
#
#     # Output 3
#     Output(component_id='3', component_property=OutputTypeClass.children),
#
#     # Output 4
#     Output(component_id='4', component_property=OutputTypeClass.children),
#
#     # Input 0
#     Input(component_id=InputName.input_1, component_property=InputType.value)
# )
# @validate_arguments
# def update_city_selected(input_value: str):
#     return (
#         # Output 0
#         create_simple_output(input_value_=input_value),
#
#         # Output 1
#         create_simple_output(input_value_=input_value),
#
#         # Output 2
#         create_simple_output(input_value_=input_value),
#
#         # Output 3
#         create_simple_output(input_value_=input_value),
#
#         # Output 4
#         create_simple_output(input_value_=input_value),
#     )
#



