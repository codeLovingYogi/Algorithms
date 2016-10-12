class Node:
	def __init__(self, data):
		self.left = None
		self.right = None
		self.data = data

class BinarySearchTree:
	def insert(self, root, data):
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

	def display_in_order(self, root):
		if not root:
			return
		self.display_in_order(root.left)
		print(root.data)
		self.display_in_order(root.right)

	def display_pre_order(self, root):
		if not root:
			return
		print(root.data)
		self.display_pre_order(root.left)
		self.display_pre_order(root.right)

	def display_post_order(self, root):
		if not root:
			return
		self.display_post_order(root.left)
		self.display_post_order(root.right)
		print(root.data)






