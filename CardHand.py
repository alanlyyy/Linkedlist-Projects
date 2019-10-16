from PositionalList import PositionList

class CardHand(PositionList):
    """
    A class that sorts a deck of cards by their suits using a linkedlist. 
    The user has the option to play card, add card, or iterate through all cards found in the list.
    
    Card is a subclass of CardHand:
        data = card rank
        next = link to next node
        suit = suit of the card
        
    functions:
    add_card(r,s) => r = rank, s = suit 
    play(s) => s= suit , returns and removes the top card of the hand for a given suit.
    __iter__ => iterator to traverse through all cards in list
    all_of_suits() => will return all cards of varying suits found in the hand.
    
    optional functions:
    checkAndRemove() => checks for size of suit list >0 and returns and 
    removes the top card of the hand for a given suit.
    
    returnList(card_node) => prints suit list given the head reference of card node
    
    Alan Ly 10-15-19
    
    
    """

    class Card:
        
        def __init__(self, element,suit , next):          #initialize node fields
            self.data = element                 #users element
            self._next = next                       #users next reference pointer
            self._suit = suit
            
    def __init__(self):
        
        #inherit from _DoublyLinkedBase class
        super().__init__()
        
        self._headD = None
        self._headC = None
        self._headH = None
        self._headS = None
        
        self._sizeD = 0
        self._sizeC = 0
        self._sizeH = 0
        self._sizeS = 0
        
        #create header nodes
        self.add_last(self.Card(self._sizeD,"Diamonds",None))
        self._headD = self.first().element()
        
        self.add_last(self.Card(self._sizeC,"Clubs",None))
        self._headC = self.after(self.first()).element()
        
        self.add_last(self.Card(self._sizeH,"Hearts",None))
        self._headH = self.after(self.after(self.first())).element()
        
        self.add_last(self.Card(self._sizeS,"Spades",None))
        self.headS = self.after(self.after(self.after(self.first()))).element()
        
        self.listOfCards = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]

        
    def find(self, suitList, rank):
        """Looks for the specific rank of card in a list of cards, using the head node of each suit list. 
           Returns true if card is found.
           
           suitNode is the 4 suits in the Positional list (D,H,S,C)
           
        """
        flag = False
        
        #first index of the element of suitNode
        cursor = suitList
        
        #loop the through the list found in suitNode, ex) loop through list of H.
        while cursor != None:
            
            #if rank is found in the list, break out of loop
            if cursor.data == rank:
                flag = True
                break

            cursor = cursor._next

        return flag
        
    def add_card(self,rank,suit):
        """Add card(rank,suit) to list.
        
        D = first index
        C = 2nd index
        H = 3rd index
        S = 4th index
        
        """
        cursor = self.first()
        
        while cursor != None:
        
            
            #if the suit is equal to the header node suit and rank is valid.
            if (cursor.element()._suit[0] == suit) and (str(rank) in self.listOfCards):
                
                #check if the rank of the card exists in the hand
                if self.find(self._headD,rank) == False  and (suit == 'D'):
                    
                    #create a card node and append it to the front of the list
                    newCard = self.Card(rank,suit, self._headD)
                    
                    #update the head of the list
                    self._headD = newCard
                    
                    if suit == 'D':
                    
                        self._sizeD += 1
                        
                        #update the size of D list in Suit object
                        cursor.element().data = self._sizeD
                        
                    break
                        
                #check if the rank of the card exists in the hand
                elif self.find(self._headC,rank) == False and (suit == 'C'):
                    
                    #create a card node and append it to the back of the list
                    newCard = self.Card(rank,suit, self._headC)
                    
                    self._headC = newCard
                        
                    if suit == 'C':
                        self._sizeC += 1
                        
                        cursor.element().data = self._sizeC
                        
                    break
                    
                
                #check if the rank of the card exists in the hand
                elif self.find(self._headH, rank) == False and (suit == 'H'):
                    
                    #create a card node and append it to the back of the list
                    newCard = self.Card(rank,suit, self._headH)
                    self._headH = newCard
               
                    if suit == 'H':
                        self._sizeH += 1
                        
                        cursor.element().data = self._sizeH
                    
                    break
                
                #check if the rank of the card exists in the hand
                elif self.find(self._headS,rank) == False and (suit == 'S'):
                    
                    #create a card node and append it to the back of the list
                    newCard = self.Card(rank,suit, self._headS)
                    
                    self._headS = newCard
                    
                    if suit == 'S':
                    
                        self._sizeS += 1
                        
                        cursor.element().data = self._sizeS
                        
                    break
                
                else:
                    print("Item already exists in the hand.")
            
            #update the cursor or to the next SuitNode
            cursor = self.after(cursor)
        
    def play(self,suit):
        """
            Remove and return a card from head of the suit list.
        
        """

        if suit == "D":
        
            if self._headD.data == 0:
                
                self.checkAndRemove()
                
            else:
                temp = self._headD
                
                #delete head and next element is now the head
                self._headD = self._headD._next
                return temp.data
                
        elif suit == "C":
        
            if self._headC.data == 0:
                
                self.checkAndRemove()
                    
            
            else:
                temp = self._headC
                
                #delete head and next element is now the head
                self._headC = self._headC._next
                
                return temp.data
                
        elif suit == "H":
            if self._headH.data == 0:
            
                self.checkAndRemove()
            
            else:
                temp = self._headH
                
                #delete head and next element is now the head
                self._headH = self._headH._next
                
                return temp.data
                
        elif suit == "S":
        
            if self._headS.data == 0:
            
                self.checkAndRemove()
            
            else:
                temp = self._headS
                
                #delete head and next element is now the head
                self._headS = self._headS._next
                
                return temp.data
        else:
            pass
            
    def checkAndRemove(self):
        """This function checks traverses through the suit positional list.
        When a list size greater than 0 is found cursor.element().data == 0
        return and remove an element from the suit list.
        """
        
        #start at the first node
        cursor = self.first()
                
        #check the size of each suit list node until a 0 for size is reached or the end of list is reached
        while (cursor != None) and  (cursor.element().data == 0):
            
            #update cursor to next suit
            cursor = self.after(cursor)
            
        if cursor.element()._suit[0] == "D":
            
            temp = self._headD
        
            #delete head and next element is now the head
            self._headD = self._headD._next
            
            #update the size for removing an element
            self._sizeD -= 1
            
            cursor.element().data = self._sizeD
            
            return temp.data
        
        if cursor.element()._suit[0] == "C":
            
            temp = self._headC
        
            #delete head and next element is now the head
            self._headC = self._headC._next
            
            #update the size for removing an element
            self._sizeC -= 1
            
            cursor.element().data = self._sizeC
            
            return temp.data
            
        if cursor.element()._suit[0] == "H":
            
            temp = self._headH
        
            #delete head and next element is now the head
            self._headD = self._headH._next
            
            #update the size for removing an element
            self._sizeH -= 1
            
            cursor.element().data = self._sizeH
            
            return temp.data
            
        if cursor.element()._suit[0] == "S":
            
            temp = self._headS
        
            #delete head and next element is now the head
            self._headD = self._headS._next
            
            #update the size for removing an element
            self._sizeS -= 1
            
            cursor.element().data = self._sizeS
            
            return temp.data
            
    def returnList(self,suit):
        """return the list of all the cards in the list for a specific suit.
           where suit is a head reference for the node list. ex) suit = self._headD
        
        """
        
        cursor = suit
        while cursor != None:
            print(cursor.data, cursor._suit)
            cursor = cursor._next
        
        

c = CardHand()
c.add_card("7","C")
c.add_card("K","C")
c.add_card("A","C")
c.add_card("7","S")
c.add_card("4","C")    #testing wrong input should do nothing
c.add_card("A","S")

#test remove 2 values from D
c.play("D")

#print list of nodes
c.returnList(c._headC)
