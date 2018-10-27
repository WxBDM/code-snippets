''' 
Created: 10/27/18
Author: Brandon Molyneaux
        @WxBDM
'''

class DoublyLinkedBag(object):
    
    '''This class is a doubly-linked node-based bag with the following methods:
    
add(element)
remove(element)
contains(element)
print_all()
    
-> All new nodes are added to the front.
-> Any data type is allowed to be an element.'''
    
    class Node:
        '''Creates a new node '''
        def __init__(self, element = None):
            self.next = None
            self.prev = None
            self.element = element
            self.print = self.__str__()
    
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0
    
    def _create_pointer(self):
        '''Creates a pointer node. Used for contains, remove, __str__'''
        pointer_node = self._make_new_node()
        pointer_node = self.front
        return pointer_node
    
    def _get_size(self):
        '''Gets the size of doubly linked bag. O(1)'''
        return self.size
    
    def _make_new_node(self, element = None):
        '''Creates a new node with a specified element.'''
        return DoublyLinkedBag.Node(element)
    
    def add(self, element):
        '''Adds elements to the front of the bag. Allows duplicates. O(1)'''
        
        n = self._make_new_node(element)
        
        if self.size == 0:
            self.front = self.rear = n
            self.size += 1
        else:
            n.next = self.front
            self.front.prev = self.front = n
            self.size += 1
        
    
    def contains(self, element):
        '''Linear scan to determine if an instance of element occurs. O(N)'''
        pointer = self._create_pointer()
        for i in range(self.size):
            if pointer.element == element:
                return True
            pointer = pointer.next
        return False
        
    
    def remove(self, element):
        '''Removes first instance of element using linear scan. O(N)'''
        pointer = self._create_pointer()
        
        for i in range(self.size):
            if pointer.element == element:
                if i == 0 and pointer.element == self.front.element:
                    self.front = pointer.next
                    pointer.next.prev = None
                    self.size -= 1
                    break
                elif i == self.size - 1 and \
                pointer.element == self.rear.element:
                    self.rear = pointer.prev
                    self.rear.next = None
                    self.size -= 1
                    break
                else:
                    pointer.prev.next = pointer.next
                    pointer.next.prev = pointer.prev
                    self.size -= 1
                    break
                    
            pointer = pointer.next
    
    def print_all(self):
        '''Prints the elements using __str__()'''
        print(self.__str__())
    
    def __str__(self):
        '''Puts the elements into a string and returns string.'''
        pointer = self._create_pointer() # creates pointer node.
        to_str = 'Elements of node-based Bag: ' # creates initial string
        
        for i in range(self.size):
            if i == self.size:
                break
            elif i == self.size - 1:
                to_str += str(pointer.element)
            else:
                to_str += str(pointer.element) + " -> "
            
            pointer = pointer.next
        
        return to_str
