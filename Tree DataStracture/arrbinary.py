# Binary Inplementation Using Array...

def binarytree(lst,p,c,char):
    x = lst.index(p)
    if char == 'L':
        lst[(2*x)+1] = c
    elif char == 'R':
        lst[(2*x )+2] = c

lst = [None]*(2*int(input("Enter Number of Nodes : "))+2)
lst[0] = 1
print(lst)

for i in range((len(lst)//2)-1):
    p,c,char = input().split()
    binarytree(lst,int(p),int(c),char)
print(lst)
