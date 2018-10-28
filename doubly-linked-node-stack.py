''' 
Created: 10/28/18
Author: Brandon Molyneaux
        @WxBDM
'''

class DoublyLinkedStack(object):
    
    '''This class is a doubly-linked node-based stack with the following methods:
    
push(element) -> adds to the top
pop() -> removes from top
contains(element)
print_all()

-> Any data type is allowed to be an element.'''
    
    class Node:
        '''Creates a new node '''
        def __init__(self, element = None):
            self.next = None
            self.prev = None
            self.element = element
    
    def __init__(self):
        '''Creates new instance of doubly linked queue'''
        self.front = None
        self.rear = None
        self.size = 0
    
    def _create_pointer(self, rear = False):
        '''Creates a pointer node. Default: front node.'''
        pointer_node = self._make_new_node()

        if rear:
            pointer_node = self.rear
        else:
            pointer_node = self.front
        
        return pointer_node
    
    def _get_size(self):
        '''Gets the size of the doubly linked bag'''
        return self.size
    
    def _make_new_node(self, element = None):
        '''Creates a new node with a specified element'''
        return DoublyLinkedStack.Node(element) 
    
    def push(self, element):
        '''Pushes an element to the stack'''
        n = self._make_new_node(element)
        
        if self.size == 0:
            self.front = n
            self.rear = n
            self.size += 1
            return True
        else:
            n.prev = self.rear
            self.rear.next = n
            self.rear = n
            self.size += 1
            return True
        
        return False
        
    def pop(self):
        
        pointer = self._create_pointer(rear = True)
        element = pointer.element
        
        if self.size == 1:
            self.front = None
            self.rear = None
            self.size -= 1
            return element
        else:
            self.rear = self.rear.prev
            self.rear.next = None
            self.size -= 1
            return element

    def contains(self, element):
        '''Linear scan to determine if an instance of element occurs.
        Returns True if instance is found. Otherwise return False.'''
        
        pointer = self._create_pointer()
        for i in range(self.size):
            if pointer.element == element:
                return True
            pointer = pointer.next
        return False
            
   
    def print_all(self, traverse_down = True):
        '''Prints the elements using __str__()'''
        print(self.__str__(traverse_down))
    
    def __str__(self, traverse_down):
        '''Puts the elements into a string and returns string. Can traverse
        forwards or backwards.'''

        to_str = 'Elements of node-based Stack: ' # creates initial string
        
        # creates either a pointer at front or rear.
        pointer = self._create_pointer() if traverse_down == True \
            else self._create_pointer(rear = True)
        
        # traverse through nodes
        for i in range(self.size):
            if i == self.size:
                break
            elif i == self.size - 1:
                to_str += str(pointer.element)
            else:
                to_str += str(pointer.element) + " -> "
            
            pointer = pointer.next if traverse_down == True else pointer.prev
        
        return to_str
