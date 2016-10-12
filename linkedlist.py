class Node:
	def __init__(self,data):
		self.data = data
		self.next = None

class LinkedList: 
	def __init__(self):
		self.head = None
		self.size = 0

	def insert(self, data):
		newest = Node(data)
		current = self.head
		if self.head is None:
			self.head = newest
		else:
			while current.next:
				current = current.next

			current.next = newest
		self.size += 1

	def delete_first(self):
		if self.head is None:
			print('List is empty')
		self.head = self.head.next
		self.size -= 1

	def delete(self, value):
		current = self.head
		previous = None
		while current:
			if current.data == value:
				if previous:
					previous.next = current.next
				else:
					self.head = current.next
			previous = current
			current = current.next
		self.size -= 1

	def display(self):
		current = self.head
		while current:
			print(current.data, end='')
			current = current.next

	def reverse(self):
		previous = None
		current = self.head
		while current:
			next = current.next
			current.next = previous
			previous = current
			current = next
		self.head = previous

def add_first(a_linked_list, element):
	"""Insert new element at beginning of a singly linked list L."""
	# create new node instance storing reference to element
	newest = Node(element)
	# set new node's next to reference old head node
	newest.next = a_linked_list.head
	# set linked list head to reference new node
	a_linked_list.head = newest
	# increment node count
	a_linked_list.size = a_linked_list.size + 1

def add_last(a_linked_list, element):
	"""Insert new element at end of a singly linked list L."""
	# create new node instance storing reference to element
	newest = Node(element)
	# set new node's next to reference None
	newest.next = None
	# set linked list tail to point to new node	
	a_linked_list.tail.next = newest
	# set linked list tail to reference new node
	a_linked_list.tail = newest
	# increment node count
	a_linked_list.size = a_linked_list + 1

def remove_first(a_linked_list):
	if L.head is None:
		print("List is empty")
	# set linked list head to reference new node
	a_linked_list.head = a_linked_list.head.next
	# decrement node count
	a_linked_list.size = a_linked_list.size - 1





