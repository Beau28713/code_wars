from Increment_String import increment_string
from pytest import mark

@mark.parametrize(
    "input, expected",
    [
        ("foo", "foo1"),
        ("foobar001", "foobar002"),
        ("foobar1", "foobar2"),
        ("foobar00", "foobar01"),
        ("foobar99", "foobar100"),
        ("foobar099", "foobar100"),
        ("", "1")
    ],
)
def test_increment_string(input, expected):
    assert increment_string(input) == expected
