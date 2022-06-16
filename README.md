# Wallbox QA Coding Test Solution: Unit Testing

This repo contains a solution for the Technical Test provided by Wallbox

## PROBLEMS

Write code to solve the following problems:

Item 1. A function that given 2 vectors of integers finds the first repeated number

Item 2. A function that given a path of the file system finds the first file that meets the
following requirements

a. The file owner is admin

b. The file is executable

c. The file has a size lower than 14*2^20

Item 3. A function that given a sequence of coin flips (0 is tails, 1 is heads) finds the
minimum quantity of permutations so that the sequence ends interspersed. For
example, given the sequence 0,1,1,0 how many changes are needed so that the
result is 0,1,0,1


PS.: Include Pytest unit testing with at least 2 Test Cases


## SOLUTIONS

The solution for the three problems presented is detaild below:


### Item 1

**File**: qa_unitest_solution/src/find_repeated_numbers.py

**Usage**:
find_repeated_numbers(): Parametrized Function that receives two lists and returns an integer with the first repeated number.
"First" is interpreted here as the lowest index among any of the two repeated elements.

### Item 1: PYTEST

**File**: qa_unitest_solution/tests/test_item1.py

**Usage**: pytest -v tests/test_item1.py (7 Tests)

*Each Test Case is documented as docstring in the test file.*


### Item 2

**File**: qa_unitest_solution/src/get_file_match.py

**Usage**: 
analize_path(): Parametrized function that receives a system path and returns the first file found inside that path that matches the conditions defined at PROBLEMS - Item2.

get_file_match(): Parametrized function that returns the file_path of a file if it matches the conditions and None otherwise. The class FileDetails is used to collect file information.


### Item2: PYTEST

**File**: qa_unitest_solution/tests/test_item2.py

**Usage**: pytest -v tests/test_item2.py (4 Tests)

For this solution two approaches were used:

The first is common unit testing using real files provided at the resources folder found inside the tests folder. (2 Test Cases)

The second is using dependency injection, inserting file information into the class FileDetails to simulate an object without the real file. (2 Test cases)

*Each Test Case is documented as docstring in the test file.*


### Item 3

**File**: qa_unitest_solution/src/get_min_permutations.py

**Usage**:
get_min_permutations(): Parametrized Function that receives a list of Coin Flips (list with 0s and 1s) and returns the minimum amount of permutations to change the sequence to an interspersed list.

Interspersed list: Alternating list of 0s and 1s.


### Item 3: PYTEST

**File**: qa_unitest_solution/tests/test_item3.py

**Usage**: pytest -v tests/test_item3.py (6 Tests)

*Each Test case is documented as doctring in the test file.*
