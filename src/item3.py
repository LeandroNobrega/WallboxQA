# Solution for the third problem

class NotCoinFlipsException(Exception):
	def __init__(self, sample):
		self.sample = sample
		super(NotCoinFlipsException, self).__init__(f"Given sample {self.sample} in NOT a Coint Flip list")

class EmptyListException(Exception):
	def __init__(self):
		super(EmptyListException, self).__init__("Coin Flip List cannot be empty")


def get_min_permutations(coin_flips):
	"""
	Compare given list with 2 interspersed lists to get minumum number of permutations needed to be one of them
	:param coin_flips: list with 0s and 1s representing flips of a coin
	:return int: minimum permutations required
	"""
	def generate_interspersed_lists(size):
		# Generate two interspersed lists (starting with 0 and 1) of given size
		starting_with_zero = [number % 2 for number in range(0, size)]
		starting_with_one = [number % 2 for number in range(1, size + 1)]
		print(starting_with_zero, starting_with_one)
		return starting_with_zero, starting_with_one
	
	def calculate_changes(sample_list):
		changes = 0
		for n in range(len(coin_flips)):
			if coin_flips[n] != sample_list[n]:
				changes += 1
		return changes

	if coin_flips:
		assert_coin_flips(coin_flips)
		first_case, second_case = generate_interspersed_lists(len(coin_flips))
		return min(calculate_changes(first_case), calculate_changes(second_case))
	else:
		raise EmptyListException

def assert_coin_flips(sample):
	# Make sure the sample provided is a list of 1s and 0s
	empty_list = [element for element in sample if element not in [0, 1]]
	if empty_list:
		raise NotCoinFlipsException(sample)


if __name__ == "__main__":
	"""
	Quick test execution
	For full unit test of these function please refer to the README under "Pytest"
	"""
	test_entries = [1, 0, 0, 1], [0, 1, 1, 0], [0, 1], [0, 1, 1], [0, 1, 1, 1, 1, 0, 0, 0]

	for entry in test_entries:
		print(get_min_permutations(entry))
