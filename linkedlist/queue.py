# Queue With LinkedList...

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self,data):
        self.head = Node(data)
        self.tail = self.head

    def enqueue(self,data):
        n = Node(data)
        self.tail.next = n
        self.tail = n

    def dequeue(self):
        self.head = self.head.next

    def peek(self):
        print("First Element : ",self.head.data)

    def display(self):
        t = self.head
        while(t):
            print(t.data,end=' ')
            t = t.next

obj = Queue(int(input("Enter : ")))

for i in range(4):
    obj.enqueue(int(input("Enter : ")))

obj.dequeue()
obj.peek()
obj.display()
