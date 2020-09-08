
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

root = Node(int(input()))

def binarySearch(root,data):
    if root.data >= data:
        if root.left == None:
            root.left = Node(data)
        else:
            binarySearch(root.left,data)
    else:
        if root.right == None:
            root.right = Node(data)
        else:
            binarySearch(root.right,data)
        

for i in range(5):
    binarySearch(root,int(input()))

def display(root):
    if root!=None:
        display(root.left)
        print(root.data)
        display(root.right)

def isBST(root):
    if root.left:
        if root.left.data != None:
            if root.data < root.left.data:
                return False
            else:
                return isBST(root.left)
    if root.right:
        if root.right.data != None:
            if root.data > root.right.data:
                return False
            else:
                return isBST(root.right)

    return True
    
display(root)
print(isBST(root))
