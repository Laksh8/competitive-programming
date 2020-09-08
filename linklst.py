class Node:
    def __init__(self,data):
        self.data= data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def addList(self,length):
        if length > 1:
            self.head = Node(1)
            n = self.head
            t = n

            for i in range(2,length+1):
                n = Node(i)
                t.next = n
                t = n
            t.next = None

    def display(self):
        t = self.head
        while(t != None):
            print(t.data)
            t = t.next

obj = LinkedList()
obj.addList(5)
obj.display()

