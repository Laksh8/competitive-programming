# Binary Search Tree...

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


def infix(root):
    if root :
        infix(root.left)
        print(root.data)
        infix(root.right)


def BinarySearchTree(root,data):
    if data > root.data:
        if root.right == None:
            n = Node(data)
            root.right = n
            return
        else:
            BinarySearchTree(root.right,data)
    else:
        if root.left == None:
            n = Node(data)
            root.left = n
            return
        else:
            BinarySearchTree(root.left,data)


root = Node(int(input("Enter Root Node : ")))
for i in range(10):
    BinarySearchTree(root,int(input("Enter Node : ")))

infix(root)
