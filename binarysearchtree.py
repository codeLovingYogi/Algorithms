class Node:
	"""Creation of node for a binary search tree with left/right child and data."""
	def __init__(self, data):
		self.left = None
		self.right = None
		self.data = data

class BinarySearchTree:
	""" Implements binary search tree (BST) using Node class."""


	def insert(self, root, data):
		"""Adds node to BST."""
		if root is None:
			return Node(data)
		else:
			if data <= root.data:
				cur = self.insert(root.left, data)
				root.left = cur
			else:
				cur = self.insert(root.right, data)
				root.right = cur
			return root

	def contains(self, root, value):
		"""Checks for value in BST."""
		if value == root.data:
			return True
		elif value < root.data:
			if root.left is None:
				return False
			else:
				return self.contains(root.left, value)
		else:
			if root.right is None:
				return False
			else:
				return self.contains(root.right, value)

	def display_in_order(self, root):
		"""Prints in-order display of BST."""
		if root is None:
			return
		self.display_in_order(root.left)
		print(root.data)
		self.display_in_order(root.right)

	def display_pre_order(self, root):
		"""Prints pre-order display of BST."""
		if root is None:
			return
		print(root.data)
		self.display_pre_order(root.left)
		self.display_pre_order(root.right)

	def display_post_order(self, root):
		"""Prints post-order display of BST."""
		if root is None:
			return
		self.display_post_order(root.left)
		self.display_post_order(root.right)
		print(root.data)






