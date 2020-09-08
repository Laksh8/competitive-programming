'''
lst = [0,1,2,3,4,5,6,7,8,9]

start, end ,value = 0, len(lst)-1, 7

while start <= end:
        mid = (start+end) //2
        
        if lst[mid] == value:
            print(mid)
            break
        
        elif(lst[mid]>value):
            end = mid-1

        elif(lst[mid]<value):
            start = mid + 1
'''
# Linked List :--

class Node:
        def __init__(self,data):
                self.data = data
                self.next = None

class linkedList:
        def __init__(self,data):
                self.head = Node(data)

        def createLinkedList(self,length):
                if length >= 1:                
                        self.head = Node(input("Enter Anything :-- "))
                        n = self.head
                        t = n
                        for i in range(length-1):
                                n = Node(input("Enter Anything :-- "))
                                t.next = n
                                t = n
        def display(self):
                t = self.head
                while(t):
                        print(t.data)
                        t = t.next

        def append(self,data):
                t = self.head
                while(t):
                        if t.next == None:
                                n = Node(data)
                                t.next = n
                                break
                        t = t.next

        def insert(self,data,position):
                t = self.head
                
                for i in range(position):
                        t = t.next
                        if i == position-2:
                                n = Node(data)
                                n.next = t.next
                                t.next = n
                                
                                


obj = linkedList(17)
obj.append(9)
obj.append(6)
obj.append(3)
obj.append(1)
obj.append(5)
obj.append(7)
obj.append(2)
obj.insert(71,3)
obj.display()
