from PositionalList import PositionList

def insertion_sort(A):
    """Sorts list of comparable elements in to nondecreasing order."""
    
    for k in range(1,len(A)):   #from 1 to n-1
        
        cur = A[k]              #current element to be inserted
        
        j = k                   #find correct index j for current
        
        
        
        #decrement indices until cur < than previous element or 0 index is reached
        
        while j> 0 and A[j-1] > cur:    #element A[j-1] must be after current
        
            A[j] = A[j-1]               #if previous element is larger than current element,
                                        #replace current element with previous element
                                        
            j -= 1                      
            
        A[j] = cur                  #cur is now in the right place
    
    return A


def insertion_sort_LL(L):
    """Sort PositionalList of comparable elements into non decreasing order.
    where L is type node.
    
    1. check current node < next node
    2.      if current node is < next node update pivot, else add smaller value before current node
    3.      update the pivot
    4.      repeat   
    """
    
    if len(L) > 1:
        
        #head of the list
        marker = L.first()
        
        while marker != L.last():
            
            pivot = L.after(marker)     #next node to place, used to advance the marker
            
            value = pivot.element()     #get element of next node
            
            
            if value > marker.element(): #pivot is already sorted if next node > current node
            
                marker = pivot           #advance the marker to next node
                
            else:
                
                walk = marker
                
                #loop while previous element > than the current element
                while walk != L.first() and L.before(walk).element() > value:
                    
                    #update the current marker or reference pointer with pointing to previous node
                    walk = L.before(walk)
                    
                L.delete(pivot)             #delete reference to next node, as 
                L.add_before(walk,value)    #reinsert value before walk
                
    return L
    
if __name__ == '__main__':
    
    l = [9,5,6,2,1]
    k = [9,8,7,6,5,4,3,2,1]
    print(l)
    print(insertion_sort(l))
    print(k)
    print(insertion_sort(k))

    pList = PositionList()

    pList.add_first(5)
    pList.add_first(4)
    pList.add_first(3)
    pList.add_first(2)
    pList.add_first(1)
    insertion_sort_LL(pList).printNodes()