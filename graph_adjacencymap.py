class Graph:
	"""Representation of simple graph using adjacency matrix."""
	#------------Nested Vertex class-----------------
	class Vertex:
		"""Lightweight vertex structure for a graph."""
		__slots__ = '_element'

		def __init__(self, x):
			"""Do not call constructor directly, use Graph's insert_vertex(x)."""
			self._element = x

		def element(self):
			"""Return element associated with this vertex."""
			return self._element

		# Allow vertex to be a map/set key
		def __hash__(self):
			return hash(id(self))

	#------------Nested Edge class-----------------
	class Edge:
		"""Lightweight edge structure for a graph."""
		__slots__ = '_origin', '_destination', '_element'

		def __init__(self, u, v, x):
			"""Do not call constructor directly, use Graph's insert_edge(u, v, x)."""
			self._origin = u
			self._destination = v
			self._element = x

		def endpoints(self):
			"""Return (u,v) tuple for vertices u and v."""
			return (self._origin, self._destination)

		def opposite(self, v):
			"""Return the vertex opposite v on this edge."""
			return self._destination if v is self._origin else self._origin

		def element(self):
			"""Return element associated with edge."""
			return self._element

		# Allow edge to be a map/set key
		def __hash__(self):
			return hash((self._origin, self._destination))

	#------------Graph methods-----------------
	def __init__(self, directed = False):
		"""Create an empty graph, undirected by default.
		Graph is directed if optional parameter set to True.
		"""
		self._outgoing = {}
		# Only create second map for directed graph, use alias for undirected
		self._incoming = {} if directed else self._outgoing

	def is_directed(self):
		"""Return True if this is a directed graph, False if undirected.

		Property based on original declaration of graph, not its contents.
		"""
		# Directed if maps are distinct
		return self._incoming is not self._outgoing

	def vertex_count(self):
		"""Return number of vertices in graph."""
		return len(self._outgoing)

	def vertices(self):
		"""Return iteration of all vertices of graph."""
		return self._outgoing.keys()

	def edge_count(self):
		"""Return number of edges in graph."""
		total = sum(len(self._outgoing[v]) for v in self._outgoing)
		# Avoid double-count of edges for undirected graphs
		return total if self.is_directed() else total // 2

	def edges(self):
		"""Return set of all edges of graph."""
		# Avoid double-reporting edges of undirect graph
		result = set()
		for secondary_map in self._outgoing.values():
			# Add edges to resulting set
			result.update(secondary_map.values())
		return result

	def get_edge(self, u, v):
		"""Return the edge from u to v, or None if not adjacent."""
		# Return None if v not adjacent
		return self._outgoing[u].get(v)

	def degree(self, v, outgoing=True):
		"""Return number of (outgoing) edges incident to vertex v in graph.

		If graph is directed, optional parameter used to count incoming edges.
		"""
		adj = self._outgoing if outgoing else self._incoming
		return len(adj[v])

	def incident_edges(self, v, outgoing=True):
		"""Return all (outgoing) edges incident to vertex v in graph.

		If graph is directed, optional parameter used to request incoming edges.
		"""
		adj = self._outgoing if outgoing else self._incoming
		for edge in adj[v].values():
			yield edge

	def insert_vertex(self, x=None):
		"""Insert and return a new Vertex with element x."""
		v = self.Vertex(x)
		self._outgoing[v] = {}
		if self.is_directed():
			# Distinct map for incoming edges
			self._incoming[v] = {}
		return v

	def insert_edge(self, u, v, x=None):
		"""Insert and return new Edge from u to v with auxilliary element x."""
		e = self.Edge(u, v, x)
		self._outgoing[u][v] = e
		self._incoming[v][u] = e
	





