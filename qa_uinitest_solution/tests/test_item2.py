import random
import pytest
from ..src.get_file_match import *

resources_path = os.path.join(os.path.dirname(__file__), "resources")
folder_default = "default_files"
folder_large = "large_files"

"""
For these tests we would need files that match different conditions to make sure all of the scenarios are tested
List of files needed:
- FILE1: Correct file (admin owner, executable, small)
- FILE2: Correct file + change owner
- FILE3: Correct file + not executable
- FILE4: Correct file + large (optional: change threshold to a smaller value for testing)
- Test all the files above into the same folder

## However, this repo does not provide all the necessary files for complete testing. ##

This repo has 2 Test Cases using real files (resources folder) and 2 Test Cases using Dependency Injection

A simulated class for the FileDetails was created, adding objects according the list above and thus proceeding
with the unit tests.
This approach would assume that the ability of getting the information from the files is working,
focusing only on the logic behind the information analysis.
"""

## UNIT TESTS

def test_basic():
    # Test with 2 files that match condition
    file_path = os.path.join(resources_path, folder_default)
    assert analyze_path(file_path), "Function failed to get the file information correctly"

def test_large_file():
    # Test with 1 default file and 1 large file. Default size threshold will be reduced to 1500 Kb for this test.
    file_path = os.path.join(resources_path, folder_large)
    assert analyze_path(file_path, size_threshold=1500000), "Function failed to get the file information correctly"


## DEPENDENCY INJECTION

@pytest.fixture
def default_file_details():
    folder_path = os.path.join(resources_path, folder_default)
    file_path = os.path.join(folder_path, "test_file1")
    return FileDetails(file_path)

def test_diff_owner(default_file_details):
    # Test with different owner
    default_file_details._owner = 'guest'
    assert not get_file_match(default_file_details), "Function failed to get the file information correctly"

def test_not_executable(default_file_details):
    # Test with file that match conditions
    default_file_details._is_executable = False
    assert not get_file_match(default_file_details), "Function failed to get the file information correctly"
