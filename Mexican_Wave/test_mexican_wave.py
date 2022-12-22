import pytest
from mexican_wave import wave


@pytest.mark.parametrize(
    "input, exspected",
    [
        ("hello", ["Hello", "hEllo", "heLlo", "helLo", "hellO"]),
        ("a       b    ", ["A       b    ", "a       B    "]),
    ],
)
def test_wave(input, exspected):
    assert wave(input) == exspected
