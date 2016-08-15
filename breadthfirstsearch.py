def BFS()(grph, s, discovered):
	"""Perform BFS of undiscovered portion of Graph grph starting at Vertex s.

	discovered is a dictionary mapping each vertex to the edge that was used to discover it during BFS. (s should be mapped to None prior to the call).
	Newly discovered vertices added to dictionary as a result.
	"""
	# first level includes only s
	level = [s]
	while len(level) > 0:
		# next level for newly found vertices
		next_level = []
		for u in level:
			# for every outgoing edge from u
			for e in grph.incident_edges(u):
				v = e.opposite(u)
				# v is an unvisited vertex
				if v not in discovered:
					# e is tree edge that discovered v
					discovered[v] = e
					# v will be explored in next pass
					next_level.append(v)
		# relabel next level to become current
		level = next_level