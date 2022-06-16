import random
from ..src.get_min_permutations import get_min_permutations, NotCoinFlipsException, EmptyListException


def test_basic_one():
    # Basic test starting with one
    flips = [1, 0, 0, 1]
    assert get_min_permutations(flips) == 2, "Failed to find the minimum number of permutations"

def test_basic_zero():
    # Basic test starting with zero
    flips = [0, 1, 1, 0]
    assert get_min_permutations(flips) == 2, "Failed to find the minimum number of permutations"

def test_size_one():
    flips = [1]
    assert get_min_permutations(flips) == 0, "Failed to find the minimum number of permutations"

def test_empty_entry():
    flips = []
    try:
        assert get_min_permutations(flips), "Function should have raised EmptyListException"
    except EmptyListException:
        pass

def test_wrong_entry():
    flips = [1, 0, 2]
    try:
        assert get_min_permutations(flips), "Function should have raised NotCoinFlipsException"
    except NotCoinFlipsException:
        pass

def test_random_entry():
    # Test to analyze execution of larger numbers
    MAX_SIZE = 100
    size = random.randint(0, MAX_SIZE)
    random_entry = [random.randint(0, 1) for _ in range(size)]
    get_min_permutations(random_entry)
