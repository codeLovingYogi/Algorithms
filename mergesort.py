def merge(a, b, a_list):
	""" Merge two sorted lists a and b into a_list."""
	# pointers to traverse through a and b
	i = j = 0
	while i + j < len(a_list):
		# if we reach end of array b, copy remaining elements from a
		# always take the smaller of two elements from both arrays
		if j == len(b) or (i < len(a) and a[i] < b[j]):
			a_list[i+j] = a[i]
			i+=1
		else:
			a_list[i+j] = b[j]
			j+=1

def merge_sort(a_list):
	"""Sort elements of a_list using merge-sort algorithm."""
	n = len(a_list)

	# list is already sorted
	if n < 2:
		return

	# divide: split list
	mid = n // 2
	# copy first half of list
	a = a_list[0:mid]
	# copy second half of list
	b = a_list[mid:n]

	# conquer recursively
	merge_sort(a)
	merge_sort(b)

	# merge sorted halves back into a_list
	merge(a, b, a_list)

