class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self,data):
        self.head = Node(data)

    def create(self,length):
        t = n = self.head
        for i in range(length-1):
            n = Node(int(input()))
            t.next = n
            t = n
    def display(self):
        t = self.head
        while t:
            print(t.data,end=" ")
            t = t.next

    def append(self,data):
        t = self.head
        while t:
            if t.next == None:
                n = Node(data)
                t.next = n
                t = n
                return 
            t = t.next
    def insert(self,pos,data):
        i = 1
        t = self.head
        while t:
            if i == pos:
                n = Node(data)
                n.next = t.next
                t.next = n
            t = t.next
            i +=1

    def search(self,data):
        i = 0
        t = self.head
        while t:
            if t.data == data:
                return i
            t = t.next
            i+=1
        return "Does't Contain data in the LinkedList..."


obj = LinkedList(int(input()))
obj.create(5)
obj.display()
obj.append(int(input("Enter Data You Want to append :-- ")))
obj.insert(2,99)
obj.display()
print(obj.search(99))
