# Fight for Laddus :




for _ in range(int(input())):
    n = int(input())
    lst = list(map(int,input().split()))
    dic = {}
    for i in range(n):
        try :
            dic[lst[i]] += 1
        except:
            dic[lst[i]] = 1
    for i in range(n):
        check = True
        for j in range(i,n):
            if dic[lst[i]] < dic[lst[j]]:
                check = False
                print(lst[j],end=" ")
                break
        if check:
            print(-1,end=" ")
    print()
            
'''
for _ in range(int(input())):
    n = int(input())
    lst = list(map(int,input().split()))
    for i in range(n):
        check = True
        for j in range(i,n):
            if lst.count(lst[i]) < lst.count(lst[j]):
                check = False
                print(lst[j],end=" ")
                break
        if check:
            print(-1,end=" ")
    print()
'''
