# Find the minimum number of ingredients :

# Number of test cases...
for _ in range(int(input())):
    ing = []
    n,t = map(int,input().split()) 
    for i in range(n):
        ing.append(list(map(int,input().split())))
        
    for _ in range(t):
        ans = []
        val = list(map(int,input().split()))
        for i in range(n):
            for j in range(i,n):
                lst = ing[i:j+1]
                temp = [0,0,0]
                for i in range(len(lst)):
                    temp[0] += lst[i][0]
                    temp[1] += lst[i][1]
                    temp[2] += lst[i][2]
                    
                if temp == val:
                    ans.append(lst)
        if not ans:
            print(-1)
            break
        minlen = ans[0]
        for an in ans:
            if len(minlen) > len(an):
                minlen = an
        for val in minlen:
            print(ing.index(val)+1,end=" ")
        print()
        




