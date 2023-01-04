from pytest import mark
from Count import count

@mark.parametrize("input, expected", [("aba", {'a': 2, 'b': 1})])

def test_count(input, expected):
    assert count(input) == expected