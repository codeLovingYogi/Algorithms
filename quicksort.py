def quick_sort(a_list, left, right):
	"""Sort list from a_list[left] to a_list[right] inclusive using quick-sort."""
	# range is sorted
	if left >= right: 
		return
	# last element of range is pivot
	pivot = a_list[right]
	# use to scan rightward
	l = left
	# use to scan leftward
	r = right - 1
	while l <= r:
		# scan from left until value >= pivot (or right marker)
		while l <= r and a_list[l] < pivot:
			l += 1
		# scan from right until value <= pivot (or left marker)
		while l <= r and a_list[r] > pivot:
			r -= 1
		# swap values if l and r pointers have not crossed
		if l <= r:
			a_list[l], a_list[r] = a_list[r], a_list[l]
			l, r = l + 1, r - 1

	# put pivot in correct place (marked by l index)
	a_list[l], a_list[right] = a_list[right], a_list[l]
	# make recursive calls
	quick_sort(a_list, left, l - 1)
	quick_sort(a_list, l + 1, right)