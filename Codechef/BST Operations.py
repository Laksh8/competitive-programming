# BST Operations :--

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def BST(root,data):
    if root.data > data:
        if root.left:
            BST(root.left,data)
        else:
            root.left = Node(data)
    else:
        if root.right:
            BST(root.right,data)
        else:
            root.right = Node(data)

def minval(root):
    if root:
        if root.left:
            return minval(root.left)
        else:
            return root

def search(root,data):
    if root.data == data:
        return root
    elif root.data > data:
        return search(root.left,data)
    else:
        return search(root.right,data)

def delete(root,data):
    temp = search(root,data)
    if not temp.left and not temp.right:
        temp = None
    elif not temp.right:
        temp.data = temp.left.data
    elif not temp.left:
        temp.data = temp.right.data
        
    else:
        val = minval(temp.right)
        temp.data = val.data
        val = None



def display(root):
    if root:
        display(root.left)
        print(root.data)
        display(root.right)
'''
t = int(input())
inp = input().split()
root = Node(int(inp[1]))
for _ in range(t-1):
    inp = input().split()
    if inp[0] == 'i':
        BST(root,int(inp[1]))
    else:
        temp = search(root,int(inp[1]))
        if temp.left:
            deleteleft(temp.left)
        elif temp.right:
            deleteright(temp.right)
        else:
            delete(temp)

'''
