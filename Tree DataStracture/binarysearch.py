# Binary Search Tree...

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class binarySearchTree:
    def __init__(self,data):
        self.root = Node(data)

    def create(self,root,data):
        if root.data >= data:
            if root.left :
                self.create(root.left,data)
            else:
                root.left = Node(data)
        else:
            if root.right:
                self.create(root.right,data)
            else:
                root.right = Node(data)
    def search(self,root,data):
        if root.data == data:
            print("Yes")
            return
        else:
            if root.data >= data:
                return self.search(root.left,data)
            else:
                return self.search(root.right,data)
        
        print("None")
        return

    def check(self,root):
        if root.right != None:
            return self.check(root.right)
        return root
    
    def delete(self,root,data):
        if root.data == data:
            x = root
            if root.left != None:
                val = self.check(root.left)
            x.data = val.data
            val.data = None
        else:
            if root.data >= data:
                return self.delete(root.left,data)
            else:
                return self.delete(root.right,data)
    
    def display(self,root):
        if root:
            self.display(root.left)
            print(root.data,end="  ")
            self.display(root.right)

obj = binarySearchTree(int(input()))

for _ in range(9):
    obj.create(obj.root,int(input()))
obj.delete(obj.root,3)
obj.display(obj.root)
l = obj.check(obj.root)
obj.search(obj.root,3)



