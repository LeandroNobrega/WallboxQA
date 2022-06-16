# Solution for the second problem

import os
import platform
from pathlib import Path


class OSNotSupported(Exception):
	def __int__(self):
		super(OSNotSupported, self).__int__("Current OS not supported")


# Class used to store information from a file
class FileDetails:
	"""
	Class defined to collect and process information about files on the file system
	File matching conditions are defined on the README
	"""
	def __init__(self, file_path):
		self.file_path = file_path
		self.file_info = Path(self.file_path)
		self.system = platform.system()
		self._owner = ''
		self._size = 0
		self._is_executable = False
		self.get_owner()
		self.get_size()
		self.get_exec_status()

		if self.system not in ['Linux', 'Windows']:
			raise OSNotSupported

	def get_owner(self):
		self._owner = self.file_info.owner()

	def get_size(self):
		self._size = self.file_info.stat().st_size

	def get_exec_status(self):
		"""
		Find if file is executable.
		Each OS has a specific handling for this property
		:return: True if is executable, False otherwise
		"""
		if 'linux' in self.system.lower():
			self._is_executable = os.access(self.file_path, os.X_OK)
		elif 'windows' in self.system.lower():
			self._is_executable = os.access(self.file_path, os.X_OK) and self.file_path.endswith(".exe")

	@property
	def owner(self):
		return self._owner

	@property
	def size(self):
		return self._size

	@property
	def is_executable(self):
		return self._is_executable
