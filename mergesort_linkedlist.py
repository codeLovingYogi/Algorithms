from linkedqueue import LinkedQueue

def merge_queue(a, b, a_queue):
	""" Merge two sorted queues a and b into a_queue."""
	while not a.is_empty() and not b.is_empty():
		# always take the smaller of two elements from both arrays
		if a.first() < b.first():
			a_queue.enqueue(a.dequeue())
		else:
			a_queue.enqueue(b.dequeue())
	# move remaining elements of a to a_queue
	while not a.is_empty():
		a_queue.enqueue(a.dequeue())
	# move remaining elements of b to a_queue
	while not b.is_empty():
		a_queue.enqueue(b.dequeue())

def merge_sort_queue(a_queue):
	"""Sort elements of a_queue using merge-sort algorithm."""
	n = len(a_queue)

	# list is already sorted
	if n < 2:
		return

	# divide: split list
	a = LinkedQueue()
	b = LinkedQueue()
	# move first n//2 elements to a
	while len(a) < n // 2:
		a.enqueue(a_queue.dequeue())
	# move rest of elements to b
	while not a_queue.is_empty():
		b.enqueue(a_queue.dequeue())
	
	# conquer recursively
	merge_sort_queue(a)
	merge_sort_queue(b)

	# merge sorted halves back into a_queue
	merge_queue(a, b, a_queue)

