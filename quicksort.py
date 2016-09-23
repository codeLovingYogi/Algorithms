def quick_sort(a_list, left, right):
	"""Sort list from a_list[left] to a_list[right] inclusive using quick-sort."""
	# range is sorted
	if left >= right: 
		return
	# last element of range is pivot
	pivot = a_list[right]
	# use to scan rightward
	q = left
	# use to scan leftward
	r = right - 1
	while q <= r:
		# scan rightward until value >= pivot
		while q <= r and a_list[q] < pivot:
			q += 1
		# scan leftward until value <= pivot
		while q <= r and a_list[r] > pivot:
			r -= 1
		# swap values if left and right pointers have not crossed
		if q <= r:
			a_list[q], a_list[r] = a_list[r], a_list[q]
			q, r = q + 1, r - 1

	# swap pivot with right pointer to place in correct place
	a_list[q], a_list[right] = a_list[right], a_list[q]
	# make recursive calls
	quick_sort(a_list, left, q - 1)
	quick_sort(a_list, q + 1, right)