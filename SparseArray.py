
class SparseArray:
"""This class was created to imitate an array, but without preallocating space for empty elements.
   A doubly linked list was used to create an array.
   The node class contains:
    - element for storing the actual data
    - index for storing the index of the array
    - prev or the previous reference
    - next or the next reference
    
    __setitem__ takes input, and index and inserts item into list in order by index
    __getitem__ returns the element given an index
    
    The run time for both functions is O(M)
    
    Alan Ly 10-14-2019

"""
    
    class _Node:
        
        __slots__ = '_element', '_index',  '_prev', '_next'    #saves memory and faster access
        
        def __init__(self, element, index, prev, next):    #initialize node fields
            self._element = element                 #users element
            self._prev = prev                       #users previous reference pointer
            self._next = next                       #users next reference pointer
            self._index = index                     #store the index of an array
            
    def __init__(self):
        self._header = self._Node(None, None, None,None) #head sentinel node
        self._trailer = self._Node(None,None,None,None)  #tail sentinel node
        self._header._next = self._trailer          #trailer is after header, 
        self._trailer._prev = self._header          #header is after trailer
        self._size = 0
    
    #O(M)
    def __setitem__(self,index,element):
        """Set node to include both element and index."""
        
        #if list is empty input index as first node in the list
        if self._size == 0:
            self._header._next = self._Node(element, index, self._header,self._trailer)
            self._trailer._prev = self._header._next
            self._size += 1
        else:
            #start at first element
            cursor = self._header._next
            
            while cursor != None:
                
                #if index is the same as cursor index overwrite existing element
                if cursor._index == index:
                
                    cursor._element = element
                    print(cursor._element)
                    
                    break
               
                #if the value of the current cursor is larger than the input index, insert element 
                #before the current index
                #if boundary case, or cursor == trailer sentinel add to the end of the list
                
                elif (cursor == self._trailer) or (cursor._index > index):

                    prev = cursor._prev 
                    
                    #previous node points to new node
                    prev._next = self._Node(element,index, prev,cursor)
                    
                    #update cursor previous reference with new node
                    cursor._prev  = prev._next
                    
                    self._size += 1
                    
                    break
                    
                else:
                    pass
                
                
                #update the cursor with next node
                cursor = cursor._next
                    
    #O(M)
    def __getitem__(self,index):
        
        cursor = self._header._next
        
        while cursor != None:
            
            #return element if index is found in list
            if cursor._index == index:
                return cursor._element
            
            #update the cursor
            cursor = cursor._next
        
        #return nothing if index does not exist in the list.
        return None
        
    def printNodes(self):
        """Traverse list and print the elements in the list"""
        elements = [None]*self._size
        
        firstNode = self._header._next      #first actual data node
        lastNode = self._trailer
        
        for index in range(0, self._size):
        
            #append node as long as the firstNode is not equal to last Node
            elements[index] = (firstNode._element, firstNode._index)
            
            #update the pointer to the next element for traversing the list
            firstNode = firstNode._next
            
        print(elements)

if __name__ = "__main__":
    SA = SparseArray()
    SA.__setitem__(9,"Alan")
    SA.__setitem__(3,"Bob")
    SA.__setitem__(4,"Jill")
    SA.__setitem__(5,"Normani")
    SA.__setitem__(7,"Te")
    SA.printNodes()
    print(SA.__getitem__(10)) #does not exist
    print(SA.__getitem__(1))