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
	a_linked_list.head = a_linked_list.head.next
	a_linked_list.size = a_linked_list.size - 1





