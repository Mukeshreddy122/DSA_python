
#linear linked list 
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        self.temp=None
        
        
        
        
    # insert elemeny at the begining of the list
    def insertAtBegining(self):
        newNode=Node(int(input("Enter the data to insert at begining:")))
        if self.head is None:
            self.head=newNode
            self.tail=newNode
            self.temp=newNode
        else:
            newNode.next=self.head
            self.head=newNode          
       
    #insert at the end of the list
    def insertAtEnd(self):
        newNode=Node(int(input("Enter the data to insert at the end:")))
        if self.head is None:
            self.head=newNode
            self.tail=newNode
            self.temp=newNode
        else:
            while self.temp.next is not None:
                self.temp=self.temp.next
            self.temp.next=newNode
            self.tail=newNode
    #insert at a specific location in the list
    def insertAtSpecificPosition(self):
        newNode=Node(int(input("Enter the data to insert at the position:")))
        position=int(input("Enter position to insert the element:"))
        if self.head is None or position<=0 or position>self.size():
            self.head=newNode
            self.tail=newNode
            self.temp=newNode
        else:
            for pos in range(position-1):
                self.temp=self.temp.next 
            newNode.next=self.temp.next
            self.temp.next=newNode.next
            
    #delete element from begining of the list
    def deleteFromBegining(self):
        self.head=self.head.next
               
                
                
                    
    # display the elements in the linked list
    def traverseLinkedList(self):
        if self.head is None:
            print("Empty list")
        else:
            while self.head is not None:
                print(self.head.data)
                self.head=self.head.next
                
LinkedListObject=LinkedList()
LinkedListObject.insertAtBegining()
LinkedListObject.insertAtEnd()
LinkedListObject.insertAtSpecificPosition()
LinkedListObject.traverseLinkedList()
        
        
        