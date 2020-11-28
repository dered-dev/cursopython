"""Linked list Exercise"""

# A single node 
class Node:
   # constructor
    def __init__(self, data = None, next = None): 
        self.data = data
        self.next = next

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

# A Linked List
class LinkedList:
    def __init__(self):  
        self.head = None

    # insertion method
    def insert(self, data):
        newNode = Node(data)
        if(self.head):
            current = self.head
            while(current.next):
                current = current.next
            current.next = newNode
        else:
            self.head = newNode

    # print method
    def printLL(self):
        current = self.head
        while(current):
            print(current.data , current.next)
            current = current.next
            
    # Delete method
    def delete(self, data):
        current = self.head
        previous = None
        found = False
        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                previous = current
                current = current.get_next()
        if current is None:
            raise ValueError("Data not in list")
        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())

# Singly Linked List

print("Init linked list")
LL = LinkedList()
print("Insert items to linked list")
LL.insert(3)
LL.insert(6)
LL.insert(5)
print("Print items of linked list")
LL.printLL()
print("Delete items to linked list")
LL.delete(3)
print("Print items of linked list")
LL.printLL()