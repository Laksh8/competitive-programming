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
        self.len = length
        if length>1:
            n = Node(input("Enter Node :-- "))
            self.head = self.tail = n
            for i in range(length-1):
                n = Node(input("Enter Node :-- "))
                self.tail.next ,n.prev,self.tail = n,self.tail,n
                
            self.head.prev,self.tail.next = self.tail , self.head

    def display(self):
        t = self.head
        for i in range(2*self.len):
            print(t.data,end=' ')
            t = t.next
        print()
        t = self.tail
        for i in range(2*self.len):
            print(t.data,end=' ')
            t = t.prev

lst = LinkedList()
lst.addList(5)
lst.display()
