class _DoublyLinkedBase:
    """A base class providing a doubly linked list representation."""
    
    class _Node:
        
        __slots__ = '_element', '_prev', '_next'    #saves memory and faster access
        
        def __init__(self, element, prev, next):    #initialize node fields
            self._element = element                 #users element
            self._prev = prev                       #users previous reference pointer
            self._next = next                       #users next reference pointer
            
    def __init__(self):
        """Create an empty list."""
        
        self._header = self._Node(None, None, None) #head sentinel node
        self._trailer = self._Node(None,None,None)  #tail sentinel node
        self._header._next = self._trailer          #trailer is after header, 
        self._trailer._prev = self._header          #header is after trailer
        self._size = 0
        
    def __len__(self):
        """Return the number of elements in the list"""
        return self._size
    
    def is_empty(self):
        """Check if the list is empty"""
        return self._size == 0
        
    def _insert_between(self, e, predecessor, successor):
        """
        Add element e between two existing nodes and return new node
        predecessor = previous node
        successor = next node
        
        By default inputs element at the end of a list
        """
        newest = self._Node(e,predecessor,successor)    #linked to neighbors
        predecessor._next = newest
        successor._prev = newest
        self._size += 1
        return newest
        
    def _delete_node(self,node):
        """Delete a non sentinel node from the list and return in"""
        predecessor = node._prev        
        successor = node._next
        predecessor._next = successor    #set predecessor next as successor
        successor._prev = predecessor   #set succesor prev as predecessor
        
        self._size -= 1
        element = node._element         #save node for returning
        node._prev = node._next = node._element = None  #clear the element
        return element
        
    def printNodes(self):
        """Traverse list and print the elements in the list"""
        elements = [None]*self._size
        
        firstNode = self._header._next      #first actual data node
        lastNode = self._trailer
        
        
        for index in range(0, self._size):
        
            #append node as long as the firstNode is not equal to last Node
            elements[index] = firstNode._element
            
            #update the pointer to the next element for traversing the list
            firstNode = firstNode._next
            
        print(elements)
        

    
