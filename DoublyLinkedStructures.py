# -*- coding: utf-8 -*-
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
                to_str += "[" + str(pointer.element) + "] <=> "
            
            pointer = pointer.next
        
        return to_str + "]"

    @staticmethod
    def _make_new_node(element = None):
        '''Creates a new node with a specified element.'''
        return DoublyLinkedStructures.Node(element)
    
    def _check_boolean_type(self, boolean, parameter):
        if boolean:
            self._allow_duplicates = True
        elif not boolean:
            self._allow_duplicates = False
        else:
            raise AttributeError("{} parameter must be of " + \
                "boolean type".format(parameter))
        return boolean
    
    def _create_pointer(self, rear = False):
        '''Creates a pointer node. Default: front node.'''
        pointer_node = self._make_new_node()

        if rear:
            pointer_node = self.rear
        else:
            pointer_node = self.front
        
        return pointer_node

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
    '''Doubly linked stack data structure.'''
    
    def __init__(self, allow_duplicates = True):
        super(DoublyLinkedStack, self).__init__()
        self._allow_duplicates = self._check_boolean_type(allow_duplicates, 
                "allow_duplicates")
      
    def _contains(self, element):
        '''Checks to see if the element exists in the set.'''
        return self.__contains__(element)
    
    def push(self, element):
        '''Adds a node to the top of the stack. Returns True if added.
Returns False if not added (only applicable if allow_duplicates is False).'''
        node = self._make_new_node(element)
        
        # checks to see if there's a duplicate in there.
        if not self._allow_duplicates:
            if self._contains(element):
                return False
        
        if self.size == 0:
            return self._add_first_node(node)
        else:
            return self._add_rear_node(node)
        
    def pop(self):
        '''Removes the node at the top of the stack. Returns the element.'''
        if self.size == 0:
            return False
        
        if self.size == 1:
            return self._remove_final_node()
        
        return self._remove_rear_node()
    
class DoublyLinkedQueue(DoublyLinkedStructures):
    '''Queue data structure. Supports double ended queue (deque) behavior.
    Currently does *not* support cyclic behavior.'''
    
    def __init__(self, allow_duplicates = True, deque = False):
        super(DoublyLinkedQueue, self).__init__()
        
        # checks to make sure the parameters are of boolean type.
        self._allow_duplicates = self._check_boolean_type(allow_duplicates, 
                "allow_duplicates")
        self._deque = self._check_boolean_type(deque, "deque")

        # error phrase.
        self._error_phrase = "Method is for when deque = True." if \
            deque is False else "Method is for when deque = False."
        
    def _contains(self, element):
        '''Checks to see if the element exists in the set.'''
        return self.__contains__(element)
    
    def _enqueue(self, element):
        '''Enqueues an element to the rear. We use the same logic twice.'''
        # check to see if duplicates are allowed. If so, check to see if the
        #   collection contains it.
        if not self._allow_duplicates:
            if self._contains(element):
                return False 
                
        # create a new node and add it into the queue.
        node = self._make_new_node(element)
        if self.size == 0:
            return self._add_first_node(node)
        
        return self._add_rear_node(node)
        
    def enqueue(self, element):
        '''Queues an element at the rear with non-double ended queue behavior.
        Will throw an error if called and deque = True'''
        
        # if the user wants double ended queue behavior, don't use this function
        #   so, raise an error.
        if self._deque:
            raise AttributeError("{0}. ".format(self._error_phrase) + 
                "Try enqueue_front(element) or enqueue_rear(element)")
        
        return self._enqueue(element)
    
    def _dequeue(self):
        '''Dequeues the last node. We use this logic twice.'''
        if self.size == 0:
            return False
        
        if self.size == 1:
            return self._remove_final_node()
        
        return self._remove_front_node()
    
    def dequeue(self):
        '''Dequeues the front node with non-double ended queue behavior.
        Will throw an error if called and deque = True.'''
        
        # if the user wants double ended queue behavior, don't use this function
        #   so, raise an error.
        if self._deque:
            raise AttributeError("{} ".format(self._error_phrase) + 
                "Try dequeue_front() or dequeue_rear()")
                
        return self._dequeue()
    
    def enqueue_rear(self, element):
        '''Method to add to the rear for double-ended queue behavior.
        Will throw an error if called and deque = False'''
        
        if self._deque:
            self._enqueue(element)
        else:
            raise AttributeError("{} Use enqueue().".format(self._error_phrase))
    
    def dequeue_rear(self):
        '''Method to remove from the rear for double-ended queue behavior.
        Will throw an error if called and deque = False.'''
        
        if self._deque:
            return self._dequeue()
        else:
            raise AttributeError("{} Use dequeue().")
    
    def enqueue_front(self, element):
        '''Method to add to the front for double-ended queue behavior.
        Will throw an error if called and deque = False.'''
                
        if self._deque:
            node = self._make_new_node(element)

            if self.size == 0:
                return self._add_first_node(node)
            
            return self._add_front_node(node)
        else:
            raise AttributeError("{} Use enqueue().".format(self._error_phrase))
    
    def dequeue_front(self):
        '''Method to remove front for double-ended queue behavior.
        Will throw an error if called and deque = False.'''
        
        if self._deque:
            if self.size == 0:
                return False
            
            if self.size == 1:
                return self._remove_final_node()
            
            return self._remove_front_node()
        else:
            raise AttributeError("{} Use dequeue().".format(self._error_phrase))
        
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
