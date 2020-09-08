# Mirror Image...

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def createBinary(root,p,c,char):
    if not root:
        return None

    if root.data == p:
        if char == 'L':
            root.left = Node(c)
        elif char == 'R':
            root.right = Node(c)

    else:
        # Try left
        if root.left :
            createBinary(root.left,p,c,char)

        # Try Right
        if root.right:
            createBinary(root.right,p,c,char)
        
        
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data)
        inorder(root.right)





root = Node(1)
for _ in range(int(input())-1):
    p,c,char = input().split()
    createBinary(root,int(p),int(c),char)

inorder(root)
