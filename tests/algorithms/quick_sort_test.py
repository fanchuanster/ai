import pytest
from quick_sort import quick_sort
lists = [
    [1,3,2,4,7,7,10,84,5],
    [1,-1,0,0,0,0,0,1],
    [3,2,1],
    [1]
]

# Parametrized test
@pytest.mark.parametrize("arr, expected", [
    (lists[0], sorted(lists[0]))
])
def test_quick_sort(arr, expected):
    assert quick_sort(arr) == expected