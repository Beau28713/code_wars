from pytest import mark
from Score import score


@mark.parametrize(
    "input, expected",
    [
        ([2, 3, 4, 6, 2], 0),
        ([4, 4, 4, 3, 3], 400),
        ([2, 4, 4, 5, 4], 450),
        ([1, 1, 1, 1, 5], 1150),
        ([1, 5, 1, 3, 4], 250),
    ],
)
def test_score(input, expected):
    assert score(input) == expected
