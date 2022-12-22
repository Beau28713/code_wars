import pytest
from first_none_repeating import first_none_repeating_letter


@pytest.mark.parametrize("test_imput, exspected", [("a", "a"), ("stress", "t"), ("moonmen", "e"), ("abba", ""), ("", ""), ("sTreSS", "T")])
def test_first_none_repeating_letter(test_imput, exspected):
    assert first_none_repeating_letter(test_imput) == exspected