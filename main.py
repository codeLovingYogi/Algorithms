from mergesort import merge, merge_sort
from linkedstack import linked_stack
from linkedqueue import linked_queue
from mergesort_linkedlist import merge_queue, merge_sort_queue
from quicksort_linkedlist import quick_sort_queue
from quicksort import quick_sort
from bucketsort import bucket_sort
from quickselect import quick_select
from graph_adjacencymap import Graph
from depthfirstsearch import DFS, construct_path, DFS_complete
from breadthfirstsearch import BFS
from binarysearch import binary_search
from arraystack import ArrayStack
from linkedlist import LinkedList
from binarysearchtree import BinarySearchTree


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
# my_stack = linked_stack()
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
# my_queue = linked_queue()
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
# my_quickqueue = linked_queue()
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

# my_quickqueue2 = linked_queue()
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

# # Adjacency Map Graph
# print('*****Graph - Adjacency Map testing*****')
# edges = (('A','B'), ('A','E'), ('A','F'), ('B', 'E'), ('F','B'), ('Z','Y'))
# my_graph = Graph()
# vertices = set()
# for e in edges:
# 	vertices.add(e[0])
# 	vertices.add(e[1])

# verts = {}
# for v in vertices:
# 	verts[v] = my_graph.insert_vertex(v)

# for e in edges:
# 	src = e[0]
# 	dest = e[1]
# 	my_graph.insert_edge(verts[src], verts[dest])
# print('is directed: ', my_graph.is_directed())
# print('vertex count: ', my_graph.vertex_count())
# print('vertices: ', my_graph.vertices())
# print('edge count: ', my_graph.edge_count())
# print('edges: ', my_graph.edges())
# print('degree: ', my_graph.degree(verts["F"]))
# print('degree: ', my_graph.degree(verts["A"]))
# print('incident edges: ', my_graph.incident_edges(verts["A"]))

# # Depth-first Search
# print('*****Depth-first Search testing*****')
# u = verts["A"]
# dfs_result = {u : None}
# DFS(my_graph, u, dfs_result)
# print('result: ', len(dfs_result))
# path = construct_path(verts["A"], verts["F"], dfs_result)
# print('path: ', path)
# forest = DFS_complete(my_graph)
# print('length of forest: ', len(forest))

# # Breadth-first Search
# print('*****Breadth-first Search testing*****')
# s = verts["B"]
# bfs_result = {s : None}
# BFS(my_graph, s, bfs_result)
# print('result: ', len(dfs_result))

# Binary Search
# print('*****Binary Search testing*****')
# binary_list = [2, 5, 6, 43, 76, 93, 124, 300, 431, 678]
# print('List: ', binary_list)
# target = 4
# target2 = 76
# low = 0
# high = len(binary_list)-1
# found = binary_search(binary_list, target, low, high)
# print(target, 'found: ', found)
# found = binary_search(binary_list, target2, low, high)
# print(target2, 'found: ', found)

# # Array stack
# print('*****Array stack testing*****')
# my_array_stack = ArrayStack()
# print('is empty: ', my_array_stack.is_empty())
# my_array_stack.push(54)
# my_array_stack.push(26)
# my_array_stack.push(93)
# my_array_stack.push(17)
# print(len(my_array_stack))
# print(my_array_stack.top())
# print(my_array_stack.pop())
# print(my_array_stack.pop())
# print(len(my_array_stack))

# # Linked List 
# print('*****Linked list testing*****')
# myList = LinkedList()
# myList.insert(3)
# myList.insert(5)
# myList.insert(8)
# myList.insert(4)
# print(myList.size)
# myList.display()
# myList.reverse()
# print()
# myList.display()
# print()
# myList.delete_first()
# myList.display()
# print()
# myList.delete(8)
# myList.display()
# print()
# print(myList.size)

# Binary Search Tree
print('*****Binary search tree testing*****')
my_tree = BinarySearchTree()
root = None
root = my_tree.insert(root, 3)
my_tree.insert(root, 7)
my_tree.insert(root, 1)
my_tree.insert(root, 5)
my_tree.insert(root, 10)
print('in order')
my_tree.display_in_order(root)
print('pre order')
my_tree.display_pre_order(root)
print('post order')
my_tree.display_post_order(root)
val = 7
print('contains', val, my_tree.contains(root, val))
val = 2
print('contains', val, my_tree.contains(root, val))
val = 10
print('contains', val, my_tree.contains(root, val))