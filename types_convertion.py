TYPES_FUNCTIONS: dict = {'int': int, 'float': float, 'bool': bool, 'str': str}


def convert_to(value: any, value_type: str) -> any:
    return TYPES_FUNCTIONS[value_type](value)


def is_valid_type(value: any, value_type: str) -> bool:
    try:
        convert_to(value, value_type)
    except:
        return False
    return True