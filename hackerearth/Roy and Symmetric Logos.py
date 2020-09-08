# Roy and Symmetric Logos :

def check(lst,i,j):
    if lst[i][j] == lst[i][len(lst)-j-1] and lst[i][j] == lst[len(lst)-i-1][j]:
        return True
    return False
for _ in range(int(input())):
    n = int(input())
    lst = []
    for __ in range(n):
        lst.append([map(int,input().split())])
    if n %2 == 0 :
        val = True
        for i in range(n//2):
            for j in range(n//2):
                 if not check(lst,i ,j):
                     val = False

        if val:
            print("Yes")
                    
        
        
