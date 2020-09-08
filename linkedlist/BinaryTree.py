class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def BST(root,node):
    if root is None:
        root = node
    else:
        if root.data>= node.data:
            if root.left == None:
                root.left = node
            else:
                BST(root.left,node)

        else:
            if root.right == None:
                root.right = node
            else:
                BST(root.right,node)

def Inorder(root):
    if root:
        Inorder(root.left)
        print(root.data)
        Inorder(root.right)

r = Node(50)
BST(r,Node(25))
BST(r,Node(32))
BST(r,Node(41))
BST(r,Node(12))
BST(r,Node(3))
BST(r,Node(45))
BST(r,Node(76))

Inorder(r)
    
