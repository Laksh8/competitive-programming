# Stack with LinkedList

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self,data):
        self.head = Node(data)

    def push(self,data):
        n = Node(data)
        n.next = self.head
        self.head = n

    def pop(self):
        self.head = self.head.next

    def peek(self):
        print(f"Top Element is {self.head.data}")

    def display(self):
        t = self.head
        while t:
            print(t.data)
            t = t.next


obj = Stack(int(input("Enter a Number :-- ")))
for i in range(4):
    obj.push(int(input("Enter a Number :-- ")))

obj.display()
obj.pop()
obj.peek()
obj.push(9)
obj.display()
