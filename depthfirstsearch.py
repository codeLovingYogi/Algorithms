
def DFS(grph, u, discovered):
	"""Perform DFS of undiscovered portion of Graph grph starting at Vertex u.

	discovered is a dictionary mapping each vertex to the edge that was used to discover it during DFS. (u should be "discovered" prior to the call.)
	Newly discovered vertices added to dictionary as a result.
	"""
	# for every outgoing edge from u
	for e in grph.incident_edges(u):
		v = e.opposite(u)
		# v is an unvisited vertex
		if v not in discovered:
			# e is tree edge that discovered v
			discovered[v] = e
			# recursively explore from v
			DFS(grph, v, discovered)

def construct_path(u, v, discovered):
	"""Reconstruct directed path from u to v, given discovery tracked from DFS started at u.

	Returns ordered list of vertices on the path.
	"""
	# empty path by default
	path = []
	if v in discovered:
		# build list from v to u and then reverse it at the end
		path.append(v)
		walk = v
		while walk is not u:
			# find edge leading to walk
			e = discovered[walk]
			parent = e.opposite(walk)
			path.append(parent)
			walk = parent
		# reorient path from u to v
		path.reverse()
	return path

def DFS_complete(grph):
	"""Perform DFS for entire graph and return forest as a dictionary.

	forest maps each vertex v to the edge that was used to discover it. (Vertices that are roots of DFS tree are mapped to None.)
	"""
	forest = {}
	for u in grph.vertices():
		if u not in forest:
			# u is root of a tree
			forest[u] = None
			DFS(grph, u, forest)
	return forest

