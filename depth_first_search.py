
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
