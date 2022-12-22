import pytest
from format_duration import format_duration


@pytest.mark.parametrize(
    "test_input, expected",
    [
        (1, "1 second"),
        (62, "1 minute and 2 seconds"),
        (120, "2 minutes"),
        (3600, "1 hour"),
        (3662, "1 hour, 1 minute and 2 seconds"),
        (8859657, "102 days, 13 hours and 57 seconds"),
        (242062374, "7 years, 246 days, 15 hours, 32 minutes and 54 seconds"),
        (33243586, "1 year, 19 days, 18 hours, 19 minutes and 46 seconds")
    ]
)
def test_formate_duration(test_input, expected):
    assert format_duration(test_input) == expected
