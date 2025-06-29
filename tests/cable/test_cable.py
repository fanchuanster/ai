import pytest

from cable import min_cable

# Parametrized test
@pytest.mark.parametrize("states,dists,expected", [
    ([1,0,0], [1,5,6], 5),
    ([0,1,0,0,1,1,0,0], [3,5,10,12,13,23,30,38], 20),
])
def test_add_param(states,dists, expected):
    assert min_cable(states,dists) == expected