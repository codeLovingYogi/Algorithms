from linkedqueue import linked_queue

def quick_sort_queue(a_queue):
	"""Sort elements of a_queue using quick-sort algorithm."""
	n = len(a_queue)

	# list is already sorted
	if n < 2:
		return

	# divide
	# use first as arbitrary pivot
	pivot = a_queue.first()
	less = linked_queue()
	equal = linked_queue()
	greater = linked_queue()
	# divide a_queue into less than, equal to, or greater than pivot
	while not a_queue.is_empty():
		if a_queue.first() < pivot:
			less.enqueue(a_queue.dequeue())
		elif pivot < a_queue.first():
			greater.enqueue(a_queue.dequeue())
		else:
			equal.enqueue(a_queue.dequeue())
			
	# conquer using recursion
	quick_sort_queue(less)
	quick_sort_queue(greater)

	# concatenate results
	while not less.is_empty():
		a_queue.enqueue(less.dequeue())
	while not equal.is_empty():
		a_queue.enqueue(equal.dequeue())
	while not greater.is_empty():
		a_queue.enqueue(greater.dequeue())
		