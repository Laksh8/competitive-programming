
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self,node):
        self.head = self.temp = node
        
    def append(self,node):
        self.temp.data = node.data
        self.temp.next = node
        self.temp = node
        self.temp.next = None

def trav(data):
        if data:
            print(data.data)
            trav(data.next)
            
lst = LinkedList(Node(5))

lst.append(Node(3))
lst.append(Node(4))
lst.append(Node(2))
lst.append(Node(1))
lst.append(Node(7))

trav(lst.head)
