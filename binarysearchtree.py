# Binary Search Tree :--

#Node Formation
class Node:
    def __init__(self,data):
        self.data ,self.left,self.right = data,None,None



def BST(root,node):
    if root.data >= node.data:
        if root.left != None:
            BST(root.left,node)
        else:
            root.left = node

    else:
        if root.right != None:
            BST(root.right,node)
        else:
            root.right = node

def inorder(node):
    if node:
        inorder(node.left)
        print(node.data)
        inorder(node.right)

node = Node(int(input("Enter Value of Node :-- ")))

for i in range(4):
    BST(node,Node(int(input("Enter Value of Node :-- "))))

inorder(node)
