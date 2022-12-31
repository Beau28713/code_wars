from pytest import mark
from Domain_Name import domain_name


@mark.parametrize(
    "input, expected",
    [
        ("http://google.com", "google"),
        ("http://google.co.jp", "google"),
        ("www.xakep.ru", "xakep"),
        ("https://youtube.com", "youtube"),
    ],
)
def test_domain_name(input, expected):
    assert domain_name(input) == expected
