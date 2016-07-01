def quick_sort(a_list, left, right):
	"""Sort list from a_list[left] to a_list[right] inclusive using quick-sort."""
	# range is sorted
	if left >= right: 
		return
	# last element of range is pivot
	pivot = a_list[right]
	# use to scan rightward
	i = left
	# use to scan leftward
	j = right
	while i <= j:
		# scan until value >= pivot (or right marker reached)
		while i <= j and a_list[i] < pivot:
			i += 1
		# scan until value <= pivot (or left marker reached)
		while i <= j and a_list[j] > pivot:
			j -= 1
		# swap values
		if i <= j:
			a_list[i], a_list[j] = a_list[j], a_list[i]
			left, right = left + 1, right - 1

	# put pivot in correct place (marked by j index)
	a_list[j], a_list[left] = a_list[left], a_list[j]
	# make recursive calls
	quick_sort(a_list, left, j - 1)
	quick_sort(a_list, j + 1, right)

