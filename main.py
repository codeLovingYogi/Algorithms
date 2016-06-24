from mergesort import merge, merge_sort
from linkedstack import LinkedStack
from linkedqueue import LinkedQueue
from mergesort_linkedlist import merge_queue, merge_sort_queue


# merge sort
print('*****Merge-sort testing****')
my_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
print('Presorted list 1: ', my_list)
merge_sort(my_list)
print('My sorted list 1: ', my_list)
my_list = []
print('Presorted list 2: ', my_list)
merge_sort(my_list)
print('My sorted list 2: ', my_list)
my_list = [1, 2, 3]
print('Presorted list 3: ', my_list)
merge_sort(my_list)
print('My sorted list 3: ', my_list)
my_list = [100, 90, 80, 70]
print('Presorted list 4: ', my_list)
merge_sort(my_list)
print('My sorted list 4: ', my_list)

# linked stack
print('*****Linked stack testing*****')
my_stack = LinkedStack()
print('head: ', my_stack._head)
print('size: ', my_stack._size)
print('my stack: ', my_stack.display())
my_stack.push(54)
my_stack.push(26)
my_stack.push(93)
my_stack.push(17)
my_stack.push(77)
my_stack.push(31)
my_stack.push(44)
my_stack.push(55)
my_stack.push(20)
print('head: ', my_stack._head)
print('size: ', my_stack._size)
print('len: ', len(my_stack))
print('is_empty: ', my_stack.is_empty())
print('my stack: ', my_stack.display())
print('top: ', my_stack.top())
print('pop: ', my_stack.pop())
print('my stack: ', my_stack.display())

# linked queue
print('*****Linked queue testing*****')
my_queue = LinkedQueue()
print('head: ', my_queue._head)
print('tail: ', my_queue._tail)
print('size: ', my_queue._size)
print('my queue: ', my_queue.display())
my_queue.enqueue(54)
my_queue.enqueue(26)
my_queue.enqueue(93)
my_queue.enqueue(17)
my_queue.enqueue(77)
my_queue.enqueue(31)
my_queue.enqueue(44)
my_queue.enqueue(55)
my_queue.enqueue(20)
print('head: ', my_queue._head)
print('tail: ', my_queue._tail)
print('size: ', my_queue._size)
print('len: ', len(my_queue))
print('is_empty: ', my_queue.is_empty())
print('my queue: ', my_queue.display())
print('first: ', my_queue.first())
print('dequeue: ', my_queue.dequeue())
print('my queue: ', my_queue.display())	

# Merge-sort linked queue
print('*****Merge-sort linked queue testing*****')
print('my queue: ', my_queue.display())
merge_sort_queue(my_queue)
print('my sorted queue: ', my_queue.display())