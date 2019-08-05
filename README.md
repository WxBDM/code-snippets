# Code Snippets

This repository is a collection of a variety of code snippets in the python language.

<hr>

<h2><strong>3D-Basemap</strong></h2> 
This folder contains 2 files: 3d-basemap.png and 3d-basemap.py. This produces a map (currently set to the Miller projection over CONUS), as well as a z-axis depicting height. The .png file in this folder is the output if the script were to be run.
<hr>

<h2><strong>DoublyLinkedStructures.py</strong></h2>  
This is a python file that demonstrates inheritance across different types of abstract data structures (currently only stack, queue, bag, and set are available) with the underlying data structure being a doubly linked node.  
Currently, the stack class is the only class that has been thoroughly tested.

<u><h3><strong>Queue</strong></h3></u>  
Overview/Notes:  
This abstract data structure inserts a node at the end of the chain and removes from the front (left-justified). Currently this does not support cyclic queues.

Methods:  
1. enqueue(element) -> Adds an element in the node chain.
2. dequeue() -> Removes the first element in the node chain.

Demo:
```queue = DoublyLinkedQueue()
queue.enqueue(10)
queue.enqueue(32)
queue.enqueue(5)
queue.enqueue(queue.dequeue())
print(queue)
```
Out: [32] ⇔ [5] ⇔ [10]

<u><h3><strong>Stack</strong></h3></u>  
Methods:  
1. push(element) -> Adds an element at the end of the node chain.
2. pop() -> Removes the last element in the node chain.

Demo:
```stack = DoublyLinkedStack()
num = 0
for i in range(5):
  stack.push(i)

stack.pop()
stack.pop()
print(stack)
```
Out: [0] ⇔ [1] ⇔ [2]


