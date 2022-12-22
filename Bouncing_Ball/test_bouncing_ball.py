import pytest
from bouncing_ball import bouncing


@pytest.mark.parametrize("input_1, input_2, input_3,exspected", [(3, 0.66, 1.5, 3), (2, 0.5, 1, 1), (30, 0.75, 1.5, 21), (3, 0.66, 4, -1), (-1, 0.66, 1.5, -1)])
def test_bouncing_ball(input_1, input_2, input_3,  exspected):
    assert bouncing(input_1, input_2, input_3) == exspected
