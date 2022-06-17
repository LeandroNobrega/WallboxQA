# Solution for the first problem

class EntryListException(Exception):
	def __init__(self, sample, element):
		self.sample = sample
		self.element = element
		super(EntryListException, self).__init__(f"Entry lists should contain only integers."
												 f" Found element {self.element} in entry {self.sample}")

def find_repeated_numbers(first_list, second_list):
	"""
	Go through the given lists and return the number that appears first on both.
	:param first_list: list of integers
	:param second_list: list of integers
	"""
	assert_entries([first_list, second_list])
	chosen_element = None  # Variable to hold the value and the index of the first repeated number
	if first_list and second_list:
		for num in first_list:
			if num in second_list:
				# It is a repeated number!
				current_index = min(first_list.index(num), second_list.index(num))
				if chosen_element:
					if current_index < chosen_element[-1]:  # Compare the newly found index to the previos stored one
						chosen_element = (num, current_index)  # Replace the chosen element
				else:
					chosen_element = (num, current_index) # Found element stored as a tuple: (number, index)
	if chosen_element:
		return chosen_element[0]
	else:
		# The lists are completely different or empty
		return None

def assert_entries(sample_lists):
	# Make sure that the entry lists are full integer lists
	for sample in sample_lists: # 'entries' size will always be 2 for our case
		for element in sample:
			if not isinstance(element, int):
				raise EntryListException(sample, element)


if __name__ == "__main__":
	"""
	Quick test execution
	For full unit test execution please refer to the README under "Pytest"
	"""
	test_entries = [([1, 2, 3, 4], [5, 5, 5, 2]), ([1, 2, 3, 4, 5], [6, 7, 8, 9, 10]), ([1, 3, 5, 7], [7])]
	
	for entry in test_entries:
		print(find_repeated_numbers(entry[0], entry[-1]))
