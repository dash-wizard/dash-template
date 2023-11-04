

from dash import callback, Output, Input
from pydantic import validate_arguments

from naming_conventions.InputContainer import InputName, InputType
from transformations.SimpleOutput import create_simple_output
from naming_conventions.OutputContainer import OutputDataClass, OutputTypeClass


@callback(
    # Output 0
    Output(component_id=OutputDataClass.output_1, component_property=OutputTypeClass.children),

    # Output 1
    Output(component_id='1', component_property=OutputTypeClass.children),

    # Output 2
    Output(component_id='2', component_property=OutputTypeClass.children),

    # Output 3
    Output(component_id='3', component_property=OutputTypeClass.children),

    # Output 4
    Output(component_id='4', component_property=OutputTypeClass.children),

    # Input 0
    Input(component_id=InputName.input_1, component_property=InputType.value)
)
@validate_arguments
def update_city_selected(input_value: str):
    return (
        # Output 0
        create_simple_output(input_value_=input_value),

        # Output 1
        create_simple_output(input_value_=input_value),

        # Output 2
        create_simple_output(input_value_=input_value),

        # Output 3
        create_simple_output(input_value_=input_value),

        # Output 4
        create_simple_output(input_value_=input_value),
    )


