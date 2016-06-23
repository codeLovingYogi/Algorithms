class LinkedStack:
	"""LIFO Stack implementation using a singly linked list."""

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

	# stack methods
	def __init__(self):
		"""Create an empty stack."""
		# reference to head node
		self._head = None
		self._size = 0

	def __len__(self):
		"""Return the number of elements in stack."""
		return self._size

	def is_empty(self):
		"""Return True if stack is empty."""
		return self._size == 0

	def push(self, element):
		"""Add element to top of stack."""
		# create and link new node
		self._head = self._Node(element, self._head)
		self._size += 1

	def top(self):
		"""Return the element at top of stack.

		Raise Empty exception if stack is empty.
		"""
		if self.is_empty():
			raise Empty('Stack is empty')
		# top of stack is head of list
		return self._head._element

	def pop(self):
		"""Remove and return element from top of stack.

		Raise Empty exception if stack is empty.
		"""
		if self.is_empty():
			raise Empty('Stack is empty')
		last_element = self._head._element
		# reassign the head of list
		self._head = self._head._next
		self._size -= 1
		return last_element

	def display(self):
		"""Display elements of stack."""
		current = self._head
		output = ""
		# traverse through linked list
		while current:
			output += str(current._element) + " "
			current = current._next
		return output

my_stack = LinkedStack()
print('head: ', my_stack._head)
print('size: ', my_stack._size)
print('my stack: ', my_stack.display())
my_stack.push(54)
my_stack.push(26)
my_stack.push(93)
my_stack.push(17)
my_stack.push(77)
my_stack.push(31)
my_stack.push(44)
my_stack.push(55)
my_stack.push(20)
print('head: ', my_stack._head)
print('size: ', my_stack._size)
print('len: ', len(my_stack))
print('is_empty: ', my_stack.is_empty())
print('my stack: ', my_stack.display())
print('top: ', my_stack.top())
print('pop: ', my_stack.pop())
print('my stack: ', my_stack.display())
