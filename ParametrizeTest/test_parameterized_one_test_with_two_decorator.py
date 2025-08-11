import math

import pytest

@pytest.mark.parametrize("base",[1,2,3])
@pytest.mark.parametrize("exponent",[4,5,6])
def test_raising_base_to_power(base, exponent):
    result = base ** exponent
    assert  result == math.pow(base,exponent)

