from dataclasses import dataclass

import pytest

from playground import set_to_list
from playground import Layout

@dataclass
class Args:
    set_data:set|frozenset
    header:str|None
    layout:Layout

set_to_list_test_args_and_expected = [
    (Args(set({'anthony'}), None, Layout.HORIZONTAL), ['set Value', 'anthony']),
    (Args(set({'anthony'}), None, Layout.VERTICAL), [['set Value'], ['anthony']]),
    (Args(frozenset({'anthony'}), None, Layout.HORIZONTAL), ['frozenset Value', 'anthony']),
    (Args(frozenset({'anthony'}), None, Layout.VERTICAL), [['frozenset Value'], ['anthony']]),
    (Args(frozenset({'anthony', 'garcia'}), None, Layout.HORIZONTAL), ['frozenset Values', 'anthony', 'garcia']),
    (Args(frozenset({'anthony', 'garcia'}), None, Layout.VERTICAL), [['frozenset Values'], ['anthony'], ['garcia']]),
    (Args(frozenset({'anthony', 'garcia'}), 'names', Layout.HORIZONTAL), ['names', 'anthony', 'garcia']),
    (Args(frozenset({'anthony', 'garcia'}), 'names', Layout.VERTICAL), [['names'], ['anthony'], ['garcia']]),
    (Args(set({'anthony', 'garcia'}), None, Layout.HORIZONTAL), ['set Values', 'anthony', 'garcia']),
    (Args(set({'anthony', 'garcia'}), None, Layout.VERTICAL), [['set Values'], ['anthony'], ['garcia']]),
    (Args(set({'anthony', 'garcia'}), 'names', Layout.HORIZONTAL), ['names', 'anthony', 'garcia']),
    (Args(set({'anthony', 'garcia'}), 'names', Layout.VERTICAL), [['names'], ['anthony'], ['garcia']]),
]

@pytest.mark.parametrize('kargs, expected_out', set_to_list_test_args_and_expected)
def test_set_to_list_returns_expected_list_when_sorted(kargs, expected_out):
    actual = sorted(set_to_list(**kargs.__dict__))
    expected = sorted(expected_out)
    assert actual == expected

@pytest.mark.parametrize('kargs, expected_out', set_to_list_test_args_and_expected)
def test_set_to_list_header_is_first_element(kargs, expected_out):
    actual = set_to_list(**kargs.__dict__)[0]
    expected = expected_out[0]
    assert actual == expected