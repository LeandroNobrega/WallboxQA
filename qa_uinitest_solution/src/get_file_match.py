# Solution for the second problem

import os
from .file_details import FileDetails

SIZE_THRESHOLD = 14*(2**20)
ADMIN = 'admin'


class IncorrectPathException(Exception):
	def __int__(self):
		super(IncorrectPathException, self).__int__("Given system path is not a directory.")


def get_file_match(file_details, admin=ADMIN, size_threshold=SIZE_THRESHOLD):
	"""
	Get given file's information and compare to standards
	:return: Path of the matched file is found, None otherwise
	"""
	if file_details.owner == ADMIN and file_details.is_executable and file_details.size < SIZE_THRESHOLD:
		return file_details.file_path
	else:
		return None

def analyze_path(file_path, admin=ADMIN, size_threshold=SIZE_THRESHOLD):
	"""
	Find files that match conditions defined on the README, if any
	:param file_path: path of the file system
	:param str admin: admin username
	:param size_threshold: integer with file size threshold
	:return: Path of the matched file if found, None otherwise
	"""
	file_match = False
	if os.path.isdir(file_path):
		for file in os.listdir(file_path):
			full_path = os.path.join(file_path, file)
			print(full_path)
			if os.path.isfile(full_path):
				file_details = FileDetails(os.path.join(file_path, file))
				file_match = get_file_match(file_details)
			if file_match:
				return file_match
		print('No files inside given folder match the conditions')
		return None
	else:
		raise IncorrectPathException


if __name__ == "__main__":
	"""
	Quick test execution
	For full unit test execution please refer to the README under "Pytest"
	"""
	path = input("Input folder path: ")

	print(analyze_path(path))
