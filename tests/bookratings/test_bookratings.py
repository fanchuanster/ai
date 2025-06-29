import pytest

from bookratings import max_rating_books

# Parametrized test
@pytest.mark.parametrize("amount, horror_books, scifi_books, expected", [
    (50,[(5,10),(3,30),(6,20),], [(6,30),(4,30),(2,10)], 13),
    (30,[(5,5),(3,6),(6,2),], [(6,3),(4,3),(2,10)], 26),
    (32,[(12,24),(9,10),(9,10),(5,7)], [(13,7)], 31),
])
def test_add_param(amount, horror_books, scifi_books, expected):
    assert max_rating_books(amount, horror_books, scifi_books) == expected