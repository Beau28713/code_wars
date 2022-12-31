import pytest

from Stat import stat


@pytest.mark.parametrize(
    "input, expected",
    [
        (
            "01|15|59, 1|47|16, 01|17|20, 1|32|34, 2|17|17",
            "Range: 01|01|18 Average: 01|38|05 Median: 01|32|34",
        ),
        (
            "11|15|59, 10|16|16, 12|17|20, 9|22|34, 13|19|34, 11|15|17, 11|22|00, 10|26|37, 12|17|48, 9|16|30, 12|20|14, 11|25|11",
            "Range: 04|03|04 Average: 11|14|36 Median: 11|18|59",
        ),
    ],
)
def test_stat(input, expected):
    assert stat(input) == expected
