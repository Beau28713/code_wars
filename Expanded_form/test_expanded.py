import pytest
from expanded import expanded_form


@pytest.mark.parametrize(
    "input, expected", [(12, "10 + 2"), (102, "100 + 2"), (70304, "70000 + 300 + 4")]
)
def test_expanded_form(input, expected):
    assert expanded_form(input) == expected
