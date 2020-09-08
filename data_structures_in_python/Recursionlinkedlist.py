# Impementation of Linked List using recursion :--

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

head= t= n= Node(7)
for i in range(4):
    n = Node(int(input("Enter a Number :-- ")))
    t.next = n
    t = n

def Traverse(head):
    if head:
        print(head.data)
        Traverse(head.next)

    
