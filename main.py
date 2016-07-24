from mergesort import merge, merge_sort
from linkedstack import LinkedStack
from linkedqueue import LinkedQueue
from mergesort_linkedlist import merge_queue, merge_sort_queue
from quicksort_linkedlist import quick_sort_queue
from quicksort import quick_sort
from bucketsort import bucket_sort
from quickselect import quick_select
from graph_adjacencymap import Graph

# # merge sort
# print('*****Merge-sort testing****')
# my_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
# print('Presorted list 1: ', my_list)
# merge_sort(my_list)
# print('My sorted list 1: ', my_list)
# my_list = []
# print('Presorted list 2: ', my_list)
# merge_sort(my_list)
# print('My sorted list 2: ', my_list)
# my_list = [1, 2, 3]
# print('Presorted list 3: ', my_list)
# merge_sort(my_list)
# print('My sorted list 3: ', my_list)
# my_list = [100, 90, 80, 70]
# print('Presorted list 4: ', my_list)
# merge_sort(my_list)
# print('My sorted list 4: ', my_list)

# # linked stack
# print('*****Linked stack testing*****')
# my_stack = LinkedStack()
# print('head: ', my_stack._head)
# print('size: ', my_stack._size)
# print('my stack: ', my_stack.display())
# my_stack.push(54)
# my_stack.push(26)
# my_stack.push(93)
# my_stack.push(17)
# my_stack.push(77)
# my_stack.push(31)
# my_stack.push(44)
# my_stack.push(55)
# my_stack.push(20)
# print('head: ', my_stack._head)
# print('size: ', my_stack._size)
# print('len: ', len(my_stack))
# print('is_empty: ', my_stack.is_empty())
# print('my stack: ', my_stack.display())
# print('top: ', my_stack.top())
# print('pop: ', my_stack.pop())
# print('my stack: ', my_stack.display())

# # linked queue
# print('*****Linked queue testing*****')
# my_queue = LinkedQueue()
# print('head: ', my_queue._head)
# print('tail: ', my_queue._tail)
# print('size: ', my_queue._size)
# print('my queue: ', my_queue.display())
# my_queue.enqueue(54)
# my_queue.enqueue(26)
# my_queue.enqueue(93)
# my_queue.enqueue(17)
# my_queue.enqueue(77)
# my_queue.enqueue(31)
# my_queue.enqueue(44)
# my_queue.enqueue(55)
# my_queue.enqueue(20)
# print('head: ', my_queue._head)
# print('tail: ', my_queue._tail)
# print('size: ', my_queue._size)
# print('len: ', len(my_queue))
# print('is_empty: ', my_queue.is_empty())
# print('my queue: ', my_queue.display())
# print('first: ', my_queue.first())
# print('dequeue: ', my_queue.dequeue())
# print('my queue: ', my_queue.display())	

# # Merge-sort linked queue
# print('*****Merge-sort linked queue testing*****')
# print('my queue: ', my_queue.display())
# merge_sort_queue(my_queue)
# print('my sorted queue: ', my_queue.display())

# # Quick-sort linked queue
# print('*****Quick-sort linked queue testing*****')
# my_quickqueue = LinkedQueue()
# my_quickqueue.enqueue(54)
# my_quickqueue.enqueue(35)
# my_quickqueue.enqueue(23)
# my_quickqueue.enqueue(21)
# my_quickqueue.enqueue(18)
# my_quickqueue.enqueue(12)
# my_quickqueue.enqueue(9)
# print('my queue: ', my_quickqueue.display())
# quick_sort_queue(my_quickqueue)
# print('my sorted queue: ', my_quickqueue.display())

# my_quickqueue2 = LinkedQueue()
# my_quickqueue2.enqueue(21)
# my_quickqueue2.enqueue(18)
# my_quickqueue2.enqueue(12)
# my_quickqueue2.enqueue(9)
# my_quickqueue2.enqueue(54)
# my_quickqueue2.enqueue(23)
# my_quickqueue2.enqueue(35)
# print('my queue 2: ', my_quickqueue2.display())
# quick_sort_queue(my_quickqueue2)
# print('my sorted queue 2: ', my_quickqueue2.display())

# # Quick-sort
# print('*****Quick-sort testing*****')
# my_quicksort_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
# print('Presorted list: ', my_quicksort_list)
# quick_sort(my_quicksort_list, 0, len(my_quicksort_list)-1)
# print('My sorted list: ', my_quicksort_list)
# my_quicksort_list2 = []
# print('Presorted list 2: ', my_quicksort_list2)
# quick_sort(my_quicksort_list2, 0, len(my_quicksort_list2)-1)
# print('My sorted list 2: ', my_quicksort_list2)
# my_quicksort_list3 = [1, 2, 3]
# print('Presorted list 3: ', my_quicksort_list3)
# quick_sort(my_quicksort_list3, 0, len(my_quicksort_list3)-1)
# print('My sorted list 3: ', my_quicksort_list3)
# my_quicksort_list4 = [100, 90, 80, 70]
# print('Presorted list 4: ', my_quicksort_list4)
# quick_sort(my_quicksort_list4, 0, len(my_quicksort_list4)-1)
# print('My sorted list 4: ', my_quicksort_list4)

# # Bucket-sort
# print('*****Bucket-sort testing*****')
# sequence = [[0, "b"], [3, "c"], [0, "a"], [2, "e"], [1, "d"]]
# print('Presorted list: ', sequence)
# bucket_sort(sequence)
# print('After bucket-sort: ', sequence)

# # Quick-select
# print('*****Quick-select testing*****')
# my_quickselect_list = [24, 34, 2, 7, 12, 98, 52]
# print('List: ', my_quickselect_list)
# k = 4
# selection = quick_select(my_quickselect_list, k)
# print(k, "th element: ", selection)
# k = 6
# selection = quick_select(my_quickselect_list, k)
# print(k, "th element: ", selection)
# k = 1
# selection = quick_select(my_quickselect_list, k)
# print(k, "th element: ", selection)

# Adjacency Map Graph
print('*****Graph - Adjacency Map testing*****')
edges = (('A','B'), ('A','E'), ('A','F'))
my_graph = Graph()
vertices = set()
for e in edges:
	vertices.add(e[0])
	vertices.add(e[1])

verts = {}
for v in vertices:
	verts[v] = my_graph.insert_vertex(v)

for e in edges:
	src = e[0]
	dest = e[1]
	my_graph.insert_edge(verts[src], verts[dest])
print('is directed: ', my_graph.is_directed())
print('vertex count: ', my_graph.vertex_count())
print('vertices: ', my_graph.vertices())
print('edge count: ', my_graph.edge_count())
print('edges: ', my_graph.edges())
print('degree: ', my_graph.degree(verts["F"]))
print('degree: ', my_graph.degree(verts["A"]))
print('incident edges: ', my_graph.incident_edges(verts["A"]))



