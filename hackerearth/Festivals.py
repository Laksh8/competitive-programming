# Festivals :

for _ in range(int(input())):
    n = int(input())
    dic = {}
    for i in range(n):
        a,b = input().split()
        try :
            dic[a].append(int(b))
        except:
            dic[a] = []
            dic[a].append(int(b))
    lst = ['',0]
    keys = sorted(dic)
    for key in keys:
        val = sorted(dic[key],reverse=True)        
        if len(val) > 3:
            if lst[1] < sum(val[:3]):
                lst[0],lst[1] = key,sum(val[:3])
        else:
            if lst[1] < sum(val):
                lst[0],lst[1] = key,sum(val)

    print(lst[0],lst[1])
            
                
