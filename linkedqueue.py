class LinkedQueue:
	"""FIFO queue implementation using a singly linked list."""

	# nested _Node class
	class _Node:
		"""Lightweight, nonpublic class for storing a singly linked node."""
		# streamline memory usage
		__slots__ = '_element', '_next'

		# initialize node's fields
		def __init__(self, element, next):
			# reference to user's element
			self._element = element
			# reference to next node
			self._next = next

	# queue methods
	def __init__(self):
		"""Create an empty queue."""
		# reference to head and tail nodes
		self._head = None
		self._tail = None
		# number of queue elements
		self._size = 0

	def __len__(self):
		"""Return number of elements in queue."""
		return self._size

	def is_empty(self):
		"""Return True if queue is empty."""
		return self._size == 0

	def first(self):
		"""Return element at front of queue.

		Raise Empty exception if queue is empty.
		"""
		if self.is_empty():
			raise Empty('Queue is empty')
		# front of queue is head of list
		return self._head._element

	def dequeue(self):
		"""Remove and return first element of queue (FIFO).
		
		Raise Empty exception if queue is empty.
		"""
		if self.is_empty():
			raise Empty('Queue is empty')
		first_element = self._head._element
		# reassign the head of list
		self._head = self._head._next
		self._size -= 1
		# if queue is empty, also remove reference from tail
		if self.is_empty():
			self._tail = None
		return first_element

	def enqueue(self, element):
		"""Add element to back of queue."""
		# node will be new tail node
		newest = self._Node(element, None)
		if self.is_empty():
			self._head = newest
		else:
			self._tail._next = newest

		# update reference of tail node
		self._tail = newest
		self._size += 1
	
	def display(self):
		"""Display elements of queue."""
		current = self._head
		output = ""
		while current != None:
			output += str(current._element) + " "
			current = current._next
		return output

my_queue = LinkedQueue()
print('head: ', my_queue._head)
print('tail: ', my_queue._tail)
print('size: ', my_queue._size)
print('my queue: ', my_queue.display())
my_queue.enqueue(54)
my_queue.enqueue(26)
my_queue.enqueue(93)
my_queue.enqueue(17)
my_queue.enqueue(77)
my_queue.enqueue(31)
my_queue.enqueue(44)
my_queue.enqueue(55)
my_queue.enqueue(20)
print('head: ', my_queue._head)
print('tail: ', my_queue._tail)
print('size: ', my_queue._size)
print('len: ', len(my_queue))
print('is_empty: ', my_queue.is_empty())
print('my queue: ', my_queue.display())
print('first: ', my_queue.first())
print('dequeue: ', my_queue.dequeue())
print('my queue: ', my_queue.display())	