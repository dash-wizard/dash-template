
from pydantic import validate_arguments


@validate_arguments
def create_simple_output(input_value_: str):
    return f'You selected: {input_value_}',

