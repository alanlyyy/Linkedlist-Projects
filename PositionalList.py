from DoublyLinkedList import _DoublyLinkedBase

import time 

class PositionList(_DoublyLinkedBase):
    """A sequential container of elements allowing positional access, using a doubly linked list."""
    
    #------------------nested Position class---------------------
    
    class Position:
        """ An abstraction representing the location of a single element."""
        
        def __init__(self, container, node):
            """Constructor should not be invoked by user."""
            self._container = container
            self._node = node
            
        def element(self):
            """Return the element stored at this position."""
            
            return self._node._element
            
        def __eq__(self,other):
            """Return true if other is a position representing the same location."""
            return type(other) is type(self) and other._node is self._node
            
        def __ne__(self, other):
            """Return true if others does not represent the same location."""
            return not (self == other)  #opposite of __eq__
            
    #----------------------utility method-----------------------------
        
    def _validate(self,p):
        """Return positions node, or raise appropriate error if invalid."""
        if not isinstance(p, self.Position):
            raise TypeError('p must be proper position type')
            
        if p._container is not self:
            raise ValueError('p does not belong to this container.')
            
        if p._node._next is None:
            raise ValueError('p is no longer valid')
            
        return p._node
        
    def _make_position(self,node):
        """ Return position instance for given node (or None if sentinel node)."""
        
        #if sentinel node
        if node is self._header or node is self._trailer: #boundary violation
            return None
        else:                                               #actual position
            return self.Position(self, node)
            
    #---------------------accessors--------------------------------------
    
    def first(self):
        """Return the first position in the list (or None if list is empty)."""
        return self._make_position(self._header._next)
        
    def last(self):
        """Return the last position of list (or None if list is empty). """
        return self._make_position(self._trailer._prev)
        
    def before(self,p):
        """Return the position just before Position p (or None if p is first)."""
        node = self._validate(p)
        return self._make_position(node._prev)
        
    def after(self,p):
        """Return the position just after position p (or None if p is last)."""
        
        #throw an exception if p is not of type of position
        node = self._validate(p)
        
        return self._make_position(node._next)
        
    def __iter__(self):
        """Generate a forward iteration of the list."""
        
        #first element in the list
        cursor = self.first()
        
        #iterate the list until trailer or header sentinel is reached
        while cursor is not None:
            
            #freeze cursor at current position
            yield cursor.element()
            
            #move cursor to the next node
            cursor = self.after(cursor)
            
    def __reverse__(self):
        """Generate a backward iteration of the list."""
        
        #first element in the list
        cursor = self.last()
        
        #iterate the list until trailer or header sentinel is reached
        while cursor is not None:
            
            #freeze cursor at current position
            yield cursor.element()
            
            #move cursor to the next node
            cursor = self.before(cursor)
            
    #----------------------------mutators-------------------------------
    
    #override inherited version from _DoublyLinkedBase to return position rather than node
    
    def _insert_between(self,e, predecessor, successor):
        """Add element between existing nodes and return new position."""
        
        #super() is used to refer to base class _DoublyLinkedBase
        node = super()._insert_between(e,predecessor,successor)
        
        return self._make_position(node)
        
    def add_first(self,e):
        """insert element e at the front of the list and return new position."""
        return self._insert_between(e, self._header,self._header._next)
        
    def add_last(self,e):
        """insert element e at back of the list and return new position."""
        self._insert_between(e, self._trailer._prev, self._trailer)
        
    def add_before(self, p, e):
        """Insert element e into list before Position p and return new Position."""
        
        #check for boundary violations adding before header sentinel
        original = self._validate(p)    
        
        return self._insert_between(e, original._prev, original)
        
    def add_after(self,p,e):
        """insert element e into list after position p and return new position."""
        
        #check for boundary violation adding after trailing sentinel
        original = self._validate(p)
        
        return self._insert._between(e, original, original._next)
        
    def delete(self,p):
        """Remove and return the element at Position p."""
        
        original = self._validate(p)
        
        return self._delete_node(original)  #inherited method returns element
        
    
    def replace(self,p,e):
        """Replace the element at Position p with element e
        
        Return the element formerly at Position p.
        """
        
        #make sure position p is valid
        original = self._validate(p)
        
        #get the data from node
        old_value = original._element
        
        #overwrite the data in the node with new data
        original._element = e
        
        #return node being erased
        return old_value
    
    def max(self):
        """Find the max element in a list of comparable elements."""
    
        #sort the list
        self.insertion_sort_LL()
        
        #return the last element of the sorted list, which is the max
        return self.last().element()
        
    def insertion_sort_LL(self):
        """Sort PositionalList of comparable elements into non decreasing order.
        where L is type node.
        
        1. check current node < next node
        2.      if current node is < next node update pivot, else add smaller value before current node
        3.      update the pivot
        4.      repeat   
        """
        
        if len(self) > 1:
            
            #head of the list
            marker = self.first()
            
            while marker != self.last():
                
                pivot = self.after(marker)     #next node to place, used to advance the marker
                
                value = pivot.element()     #get element of next node
                
                
                if value > marker.element(): #pivot is already sorted if next node > current node
                
                    marker = pivot           #advance the marker to next node
                    
                else:
                    
                    walk = marker
                    
                    #loop while previous element > than the current element
                    while walk != self.first() and self.before(walk).element() > value:
                        
                        #update the current marker or reference pointer with pointing to previous node
                        walk = self.before(walk)
                        
                    self.delete(pivot)             #delete reference to next node, as 
                    self.add_before(walk,value)    #reinsert value before walk
        
        #return sorted linked list
        return self
        
    def find(self,e):
        """Returns the first position of element e found in the list, if not found return None."""
        
        
        cursor = self.first()
        
        try:
            while cursor.element() != e:
                
                #update cursor
                cursor = self.after(cursor)
        
            
            # return the position of the cursor
            return cursor
            
        except:
        
            return None
            
    def find_recursion(self,position,e):
    
        """Takes a position and recursively finds element e in a list."""
        
        #if traverse through whole list and element e is not found
        if position == None:
        
            return None
        
        #element e is found
        elif position.element() == e:
        
            return position
        
        #traverses through list by updating position in the list
        else:
        
            position = self.after(position)
            
            return self.find_recursion(position, e)
            
    def swap(self,p,q):
        """takes position p and position q references and swap them in the list."""
        
        #if elements being swapped are right next to each other
        if (p._node._next == q._node) or (q._node._next == p._node):
            
            p._node._next = q._node._next
            q._node._prev = p._node._prev
            
            if p._node._next != None:
                p._node._next._prev = p._node
                
            if q._node._prev != None:
                q._node._prev._next = q._node
            
            q._node._next = p._node
            p._node._prev = q._node
        
        #if both elements are the same position
        elif (p._node == q._node):
            pass
        
        else:
            #save before and after references for p
            p_prev = p._node._prev 
            p_next = p._node._next
            
            #save before and after references for q
            q_prev = q._node._prev
            q_next = q._node._next
            #------------------------------------------------
            #swap node p with node q
            p_prev._next = q._node
            p_next._prev = q._node
            
            #update before and after of node q
            q._node._next = p_next
            q._node._prev = p_prev
            
            #swap node q with node p
            q_prev._next = p._node
            q_next._prev = p._node
          
            #update before and after of node p
            p._node._next = q_next
            p._node._prev = q_prev
        
            

if __name__ == '__main__':
    
    LL = PositionList()
    LL.add_first(1)
    LL.add_last(2)
    LL.add_last(3)
    LL.add_last(4)
    LL.add_last(5)
    LL.add_last(6)
    LL.add_last(7)
    LL.add_last(8)
    print(LL.first().element(),LL.last().element())
    print(LL.before(LL.last()).element())
    LL.printNodes()
    
    #test list sorting 
    LL.insertion_sort_LL()
    LL.printNodes()
    
    #test sorting front and last
    print(LL.first().element(),LL.last().element()) #0, 7
    
    #return max element or last element in sorted list
    print(LL.max())
    
    #test the cursor
    print(LL.find(7))
    print(LL.find(67))

    print(LL.find_recursion(LL.first(),7))
    print(LL.find_recursion(LL.first(),67))

    
    LL.swap(LL.first(),LL.after(LL.first()))
    LL.printNodes()