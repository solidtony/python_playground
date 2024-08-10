from typing import Iterable

from .enums import Layout


def set_to_list(set_data:set|frozenset, header:str|None, layout:Layout=Layout.VERTICAL) -> list:
    if header is None:
        header = create_default_header(set_data)
    data = [header] + list(set_data)
    if layout == Layout.VERTICAL:
        data = convert_to_vertical(data)
    return data

def create_default_header(data) -> str:
    header = type(data).__name__ + ' Value'
    header += 's' if len(data) > 1 else ''
    return header

def convert_to_vertical(data:list):
    return [[value] for value in data]
