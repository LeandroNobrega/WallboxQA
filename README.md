# Wallbox QA Coding Test Solution: Unit Testing

This repo contains a solution for the Technical Test provided by Wallbox

## PROBLEMS

Write code to solve the following problems:

1. A function that given 2 vectors of integers finds the first repeated number

2. A function that given a path of the file system finds the first file that meets the
following requirements

a. The file owner is admin

b. The file is executable

c. The file has a size lower than 14*2^20

3. A function that given a sequence of coin flips (0 is tails, 1 is heads) finds the
minimum quantity of permutations so that the sequence ends interspersed. For
example, given the sequence 0,1,1,0 how many changes are needed so that the
result is 0,1,0,1


PS.: Include Pytest unit testing with at least 2 Test Cases


## SOLUTION

The solution for the three problems presented is detaild below:

### Item 1

File: src/item1.py

Usage:
find_repeated_numbers(): Parametrized Function that receives two lists and returns an integer with the first repeated number.
"First" is interpreted here as the lowest index among any of the two repeated elements.

### Item 1: PYTEST

File: test/test_item1.py

Usage: pytest -v test/test_item.py (7 Tests)

Each Test Case is documented as docstring on the test file.

 
