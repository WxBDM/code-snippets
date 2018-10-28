''' 
Created: 10/27/18
Author: Brandon Molyneaux
        @WxBDM
'''

class DoublyLinkedList(object):
    
    '''This class is a doubly-linked node-based list with the following methods:
    
add(element)
remove(element)
contains(element)
print_all()
    
Note that this requires sequential order and will not allow duplicates.

-> Only ints and floats can be the data type.'''
    
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
    
    def _create_pointer(self, rear = False):
        '''Creates a pointer node. Used for contains, remove, __str__'''
        pointer_node = self._make_new_node()
        pointer_node = self.front

        if rear:
            pointer_node = self.rear
        
        return pointer_node
    
    def _get_size(self):
        '''Gets the size of the doubly linked bag'''
        return self.size
    
    def _make_new_node(self, element = None):
        '''Creates a new node with a specified element'''
        return DoublyLinkedList.Node(element) 
    
    def add(self, element):
        '''Adds elements to the front of the bag. Allows duplicates.'''
        
        if (type(element) is not int) and (type(element) is not float):
            raise ValueError("Type must be int or float")
        
        n = self._make_new_node(element)

        if self.size == 0:
            self.front = self.rear = n
            self.size += 1
            return True
        
        # kick back if it contains and the current pointer. Eliminates
        #   code and reduces time complexity if we kick back both
        #   the current pointer and the pointer.
        pointer, element_exists, front_rear = self.contains(element,
                _check_conditions = True)        
        if element_exists:
            return False
        
        if front_rear == 'rear':
            if pointer.next == None:
                n.prev = pointer
                pointer.next = n
                self.rear = n
                self.size += 1
                return True
            else:
                n.next = pointer.next
                n.rear = pointer
                pointer.next.prev = n
                pointer.next = n
                self.size += 1
                return True
        if front_rear == 'front':
            if pointer.prev == None:
                n.next = pointer
                pointer.prev = n
                self.front = n
                self.size += 1
                return True
            else:
                n.next = pointer
                n.prev = pointer.prev
                pointer.prev.next = n
                pointer.prev = n
                self.size += 1
                return True

    def contains(self, element, _check_conditions = False):
        '''Linear scan to determine if an instance of element occurs.'''
        
        # _check_conditions is going to be our way to add a node

        p_front = self._create_pointer()
        p_rear = self._create_pointer(rear = True)
        
        for i in range(self.size):
            
            # set stuff to be true or false to reduce code below.
            # front_element is true if the element is equal to search element
            # rear_element is true if the element is equal to search element
            # meeted is true if the front and rear elements are the same.
            front_element = True if p_front.element == element else False
            rear_element = True if p_rear.element == element else False
            meeted = True if p_rear.element == p_front.element \
                    else False
                
            # if either front or rear is the element
            if front_element or rear_element:
                if front_element:
                    return p_front, True, None
                elif rear_element:
                    return p_rear, True, None
            
            if _check_conditions:
                if p_front.element > element:
                    return p_front, None, 'front'
                if p_rear.element < element:
                    return p_rear, None, 'rear'
            
            # if the two pointer elements meet in the middle.
            if meeted:
                return None, False, None # the element doesn't exist.
            
            p_front = p_front.next
            p_rear = p_rear.prev
            
    
    def remove(self, element):
        '''Removes first instance of element'''
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
        to_str = 'Elements of node-based List: ' # creates initial string
        
        for i in range(self.size):
            if i == self.size:
                break
            elif i == self.size - 1:
                to_str += str(pointer.element)
            else:
                to_str += str(pointer.element) + " -> "
            
            pointer = pointer.next
        
        return to_str