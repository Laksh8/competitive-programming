# Deletion in BST :-


class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


root = Node(int(input("Enter Root Value :- ")))

def BST(root,data):
    if root :
        if root.data < data:
            if root.right != None:
                BST(root.right,data)
            else:
                root.right = Node(data)
        else:
            if root.right != None:
                BST(root.left,data)
            else:
                root.left = Node(data)

def search(root,data):
    if root:
        if root.data == data:
            return root
        elif root.data < data:
            return search(root.right,data)
        else:
            return search(root.left,data)
    return None


def check(root):
    if root.right:
        return check(root.right)
    elif root.left:
        return check(root.left)
    else:
        return root

def deletion(root,data):
    x = search(root,data)
    if x.left != None :
        y = check(x.left)
        x.data = y.data
        y.data = None
        
        
def display(root):
    if root:
        display(root.left)
        print(root.data,end="  ")
        display(root.right)

for i in range(4):
    BST(root,int(input()))


deletion(root,5)
display(root)
