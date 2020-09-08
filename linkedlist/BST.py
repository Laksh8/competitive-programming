# Binary Search Tree :-- 
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def BST(root , node):
    if root.data >= node.data:
        if root.left == None: root.left = node
        else: BST(root.left,node)
    else :
        if root.right == None: root.right = node
        else: BST(root.right,node)

def inorder(root):
    #Inorder Display
    if root: inorder(root.left); print(root.data,end='\t'); inorder(root.right)

def preorder(root):
    if root:
        print(root.data,end ='\t');preorder(root.left);preorder(root.right)

def postorder(root):
    if root:
        preorder(root.left); preorder(root.right); print(root.data,end ='\t')

r = Node(int(input("Enter a Node :-- ")))


for i in range(5): BST(r,Node(int(input("Enter a Node :-- "))))

inorder(r);print();preorder(r);print();postorder(r)
