class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def addList(self,length):
        if length>1:
            n = Node(int(input("Enter Value :-- ")))
            self.head = n
            self.head.prev = None
            self.tail = n
            for i in range(length-1):
                n = Node(input("Enter Value :-- "))
                self.tail.next=n
                n.prev = self.tail
                self.tail = n
            self.next = None

    def display(self):
        t = self.head
        while(t):
            print(t.data,end="\t")
            t = t.next
        print()
        t = self.tail
        while(t):
            print(t.data,end="\t")
            t = t.prev

lst = LinkedList()
lst.addList(5)
lst.display()
            
