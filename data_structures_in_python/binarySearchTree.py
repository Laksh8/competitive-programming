class Node:
    def __init__(self,data):
        self.root = data
        self.left = self.right = None

def BST(root,data):
    if root.root >= data:
        if root.left == None:
            n = Node(data)
            root.left = n
        else:
            BST(root.left,data)

    else:
        if root.right == None:
            n = Node(data)
            root.right = n
        else:
            BST(root.right,data)


def inorder(root):
    if root:
        inorder(root.left)
        print(root.root)
        inorder(root.right)

def postorder(root):
    if root:
        print(root.data)
        postorder(root.left)
        postorder(root.right)

def preorder(root):
    if root:
        preorder(root.left)
        preorder(root.right)
        print(root.data)



root = Node(int(input("Enter a Number :-- ")))

for i in range(9):
    BST(root,int(input("Enter a Number :-- ")))

inorder(root)
