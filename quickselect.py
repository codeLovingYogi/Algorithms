import random

def quick_select(a_list, k):
	"""Return the kth smallest element from a_list, for k from 1 to len(a_list)."""
	if len(a_list) == 1:
		return a_list[0]
	# Pick random pivot element from a_list
	pivot = random.choice(a_list)
	# Elements less than pivot
	L = [x for x in a_list if x < pivot]
	# Elements more equal to pivot
	E = [x for x in a_list if x == pivot]
	# Elements greater than pivot
	G = [x for x in a_list if pivot < x]

	if k <= len(L):
		# kth smallest in L
		return quick_select(L, k)
	elif k <= len(L) + len(E):
		# kth smallest equals pivot
		return pivot
	else:
		# new selection parameter
		j = k - len(L) - len(E)
		# kth smallest is jth in G
		return quick_select(G, j)

