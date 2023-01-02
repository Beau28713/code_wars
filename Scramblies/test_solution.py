from pytest import mark
from solution import scramble


@mark.parametrize(
    "input_1, input_2, expected",
    [
        ("rkqodlw", "world", True),
        ("cedewaraaossoqqyt", "codewars", True),
        ("katas", "steak", False),
        ("scriptjava", "javascript", True),
        ("scriptingjava", "javascript", True),
        ("cmketehwcwosk", "swww", False),
        ("abcdefghijklmnopqrstuvwxyz" * 500, "zyxcba" * 250, True),
    ],
)
def test_scramble(input_1, input_2, expected):
    assert scramble(input_1, input_2) == expected
