def binary_search(data, target, low, high):
	"""Return true if target found in data.

	Search only considers portion from data[low] to data[high].
	"""
	# interval empty, no match
	if low > high:
		return False
	else:
		mid = (low + high) // 2
		# match found
		if target == data[mid]:
			return True
		elif target < data[mid]:
			# recurse on first half of data
			return binary_search(data, target, low, mid - 1)
		else:
			# recurse on second half of data
			return binary_search(data, target, mid + 1, high)

