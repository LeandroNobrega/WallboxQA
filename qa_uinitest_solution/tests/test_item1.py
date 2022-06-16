import random
from ..src.find_repeated_numbers import find_repeated_numbers, EntryListException


def test_basic():
    # Basic test, same size lists
    entry1 = [1, 2, 3, 4]
    entry2 = [0, 1, 2, 3]
    assert find_repeated_numbers(entry1, entry2) == 1, "Failed to find the first repeated number"

def test_diff_sizes():
    # Basic test, different sized lists
    entry1 = [1, 2, 3, 4, 5, 6, 7, 8]
    entry2 = [9, 0, 8, 1]
    assert find_repeated_numbers(entry1, entry2) == 1, "Failed to find the first repeated number"

def test_size_one():
    # Second list has size 1
    entry1 = [1, 2, 3, 4, 5, 6, 7, 8]
    entry2 = [5]
    assert find_repeated_numbers(entry1, entry2) == 5, "Failed to find the first repeated number"

def test_empty_entry():
    # First list is empty
    entry1 = []
    entry2 = [0, 9, 8, 7, 6]
    assert not find_repeated_numbers(entry1, entry2), "Function should have returned None"

def test_different_entries():
    # Lists are different
    entry1 = [1, 2, 3, 4, 5]
    entry2 = [6, 7, 8, 9, 0]
    assert not find_repeated_numbers(entry1, entry2), "Function should have returned None"

def test_wrong_entry():
    # Second entry has a string
    entry1 = [1, 2, 3, 4, 5]
    entry2 = [6, 7, "A", 9, 0]
    try:
        assert find_repeated_numbers(entry1, entry2), "Function should have raised EntryListException"
    except EntryListException:
        pass

def test_random_entry():
    # Test to analyze execution of larger numbers
    size = random.randint(0, 100)
    random_entry1 = [random.randint(0, size) for _ in range(size)]
    random_entry2 = [random.randint(0, size) for _ in range(size)]
    find_repeated_numbers(random_entry1, random_entry2)
