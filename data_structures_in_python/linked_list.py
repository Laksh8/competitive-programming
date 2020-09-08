class Node:
	def __init__(self,data=None):
		self.data = data
		self.next = None

class Linked_list:
    def __init__(self):
        self.head = Node()

    def append(self,data):
        new_node = Node(data)
        cur = self.head
        while cur.next!=None:
            cur = cur.next
        cur.next = new_node
    def display(self):
        elem = []
        cur = self.head
        while cur.next != None:
            cur = cur.next
            elem.append([cur.data,[cur.next]])
        print(elem)
    

obj = Linked_list()
obj.append(data=5)
obj.append(data=6)
obj.append(data=7)
obj.display()

