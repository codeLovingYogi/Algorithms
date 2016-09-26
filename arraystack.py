class ArrayStack:
	"""LIFO stack implementation using Python list as underlying storage."""

	def __init__(self):
		"""Create empty stack."""
		# nonpublic list instance
		self._data = []

	def __len__(self):
		"""Return number of elements in stack."""
		return len(self._data)

	def is_empty(self):
		"""Return True if stack empty."""
		return len(self._data) == 0

	def push(self, e):
		"""Add element e to top of stack."""
		self._data.append(e)

	def top(self):
		"""Return (but do not remove) element at top of stack.

		Raise Empty exception if stack empty.
		"""

		if self.is_empty():
			raise Empty('Stack is empty')
		return self._data[-1]

	def pop(self):
		"""Return and remove element at top of stack.

		Raise Empty exception if stack empty.
		"""

		if self.is_empty():
			raise Empty('Stack is empty')
		return self._data.pop()