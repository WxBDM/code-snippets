class DoublyLinkedStructures(object):
    
    class Node:
        
        def __init__(self, element = None):
            self.element = element
            self.next = None
            self.prev = None
        
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0
    
    def _make_new_node(self, element = None):
        '''Creates a new node with a specified element.'''
        return DoublyLinkedStructures.Node(element)
    
    def _create_pointer(self, rear = False):
        '''Creates a pointer node. Default: front node.'''
        pointer_node = self._make_new_node()

        if rear:
            pointer_node = self.rear
        else:
            pointer_node = self.front
        
        return pointer_node
    
    def __call__(self):
        '''Prints out a few statements regarding the instance'''
        print("Class: " + self.__class__.__name__)
        print("Node elements: " + self.__str__())
        print("Size of node chain: " + str(self.size) + "\n")
    
    def __contains__(self, element):
        '''Checks to see if the element is in the chain.'''
        if self.size == 0:
            return False
        
        pointer = self._create_pointer()
        
        for i in range(self.size):
            if pointer.element == element:
                return True
            pointer = pointer.next
        
        return False
    
    def __eq__(self, other):
        '''Tests equality of size'''
        return self.size == other.size
    
    def __getitem__(self, position):
        '''Gets the element at a position'''
    
        # check to see if the position is out of bounds.
        if (position >= self.size) or (position < 0) and \
                (position < self.size * -1):
            raise IndexError("Index out of bounds.")
        
        # create the pointer
        pointer = self.__create_pointer(rear = False if position >= 0 else True)
    
        # asking for first position
        if position == 0:
            return pointer.element
        
        # sets up the range list to loop through.
        range_loop = position * -1 - 1 if position < 0 else position
        
        # loops through until the "index" is achieved.
        for i in range(range_loop):
            pointer = pointer.prev if position < 0 else pointer.next
        
        return pointer.element
    
    def __len__(self):
        '''Returns the length of the node chain.'''
        return self.size

    def __lt__(self, other):
        '''Tests if size is less than other node chain.'''
        return self.size < other.size
    
    def __str__(self):
        '''Puts the node chain into a string.'''
        to_str = ''
        
        # if the size is zero, return None.
        if self.size == 0:
            to_str += "None"
            return to_str
        
        # create the pointer.
        pointer = self._create_pointer()

        # if it's greater than 0, append string elements.
        for i in range(self.size):
            if i == self.size:
                break
            elif i == self.size - 1:
                to_str += "[" + str(pointer.element)
            else:
                to_str += "[" + str(pointer.element) + "] ⇔ "
            
            pointer = pointer.next
        
        return to_str + "]"

    def _add_first_node(self, n):
        '''Add a node if the size is zero.'''
        self.front = self.rear = n
        self.size += 1
        return True
    
    def _add_front_node(self, n):
        '''Add in a node in the front regardless of size.'''
        n.next = self.front
        self.front.prev = self.front = n
        self.size += 1
        return True
    
    def _add_rear_node(self, n):
        '''Add in a node in the rear regardless of size.'''
        n.prev = self.rear
        self.rear.next = self.rear = n
        self.size += 1
        return True
    
    def _add_middle_node(self, n, pointer):
        '''Add in a node in the middle regardless of size.'''
        pass
    
    def _remove_final_node(self):
        '''Remove one node in collection if size is 1.'''
        element = self.front.element
        self.front = self.rear = None
        self.size -= 1
        return element
    
    def _remove_rear_node(self):
        '''Remove last node regardless of size.'''
        element = self.rear.element
        self.rear = self.rear.prev
        self.rear.next = None
        self.size -= 1
        return element
    
    def _remove_front_node(self):
        '''Remove the first node regardless of size.'''
        element = self.front.element
        self.front = self.front.next
        self.front.prev = None
        self.size -= 1
        return element
    
    def _remove_middle_node(self, pointer):
        '''Removes a node in the middle regardless of size.'''
        element = pointer.element
        pointer.prev.next = pointer.next
        pointer.next.prev = pointer.prev
        self.size -= 1
        return element

class DoublyLinkedStack(DoublyLinkedStructures):
    '''Doubly linked stack data structure. 
    
    Methods:
        | push(element) => Pushes an element onto the top of the stack.
        |   Returns true if the element was added.
        | pop() => Pops the top element. Returns the number popped.
        
'''
    
    def __init__(self, allow_duplicates = True):
        super(DoublyLinkedStack, self).__init__()
        
        if allow_duplicates == True:
            self._allow_duplicates = True
        elif allow_duplicates == False:
            self._allow_duplicates = False
        else:
            raise AttributeError("allow_duplicates must be boolean type")
      
    def _contains(self, element):
        '''Checks to see if the element exists in the set.'''
        return self.__contains__(element)
    
    def push(self, element):
        '''Adds a node to the top of the stack. Returns True if added.
Returns False if not added (only applicable in the allow_duplicates = False
case).'''
        node = self._make_new_node(element)
        
        if not self._allow_duplicates:
            if self._contains(element):
                return False
        
        if self.size == 0:
            return self._add_first_node(node)
        else:
            return self._add_rear_node(node)
        
    def pop(self):
        '''removes the node at the top of the stack. Returns the element.'''
        if self.size == 0:
            return False
        
        if self.size == 1:
            return self._remove_final_node()
        
        return self._remove_rear_node()
    
class DoublyLinkedQueue(DoublyLinkedStructures):
    
    '''Queue data structure - first in last out.'''
    
    def __init__(self, cyclic = False):
        super(DoublyLinkedQueue, self).__init__()
        
    def enqueue(self, element):
        '''Queues an element at the rear'''
        node = self._make_new_node(element)

        if self.size == 0:
            self._add_first_node(node)
        else:
            self._add_rear_node(node)
    
    def dequeue(self):
        '''Dequeues the first element in queue'''
        if self.size == 0:
            return False
        
        if self.size == 1:
            return self._remove_final_node()
        else:
            return self._remove_first_node()

class DoublyLinkedBag(DoublyLinkedStructures):
    
    '''Unordered, allows duplicates.'''
    
    def __init__(self):
        super(DoublyLinkedBag, self).__init__()
    
    def add(self, element):
        node = self._make_new_node(element)
        
        if self.size == 0:
            self._add_first_node(node)
        else:
            self._add_rear_node(node)
    
    def remove(self, element):
        '''Removes the specified element, if it exists'''
        if self.size == 0 or not self.contains(element):
            return False
        
        pointer = self._create_pointer()
        
        for i in range(self.size):
            if pointer.element == element:
                if i == self.size - 1:
                    return self._remove_rear_node()
                return self._remove_middle_node(pointer)
            pointer = pointer.next
        
        
    
    def contains(self, element):
        '''Checks to see if the element exists in the set.'''
        return self.__contains__(element)
    
class DoublyLinkedSet(DoublyLinkedStructures):
    
    '''Unordered, does not allow duplicates.'''
    
    def __init__(self):
        super(DoublyLinkedSet, self).__init__()
    
    def add(self, element):
        '''Adds a node to the set'''
        
        node = self._make_new_node(element)
                
        if self.size == 0:
            return self._add_first_node(node)
        
        if not self.contains(element):
            return self._add_rear_node(node)
          
    def remove(self, element):
        '''Removes a select element in the collection.'''
        
        if not self.contains(element) or self.size == 0:
            return False
                
        if self.size == 1:
            return self._remove_final_node()
        
        pointer = self._create_pointer()
        
        # if it's the front.
        if pointer.element == element:
            return self._remove_front_node()
        
        for i in range(self.size):
            if pointer.element == element:
                if i == self.size - 1:
                    return self._remove_rear_node()
                return self._remove_middle_node(pointer)
            pointer = pointer.next
    
    def contains(self, element):
        '''Checks to see if the element exists in the set.'''
        return self.__contains__(element)
