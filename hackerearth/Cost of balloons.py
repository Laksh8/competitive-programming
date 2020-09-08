# Cost of balloons :

for _ in range(int(input())):
    gcost,pcost = map(int,input().split())
    lst1 = []
    lst2 = lst1.copy()
    for i in range(int(input())):
        q1,q2 = map(int,input().split())
        lst1.append(q1);lst2.append(q2);
    
    if lst1.count(1) > lst2.count(1):
        count = min(gcost,pcost) * lst1.count(1) + max(pcost,gcost)*lst2.count(1) 
    else:
        count = min(pcost,gcost)*lst2.count(1) + max(pcost,gcost) * lst1.count(1)
    print(count)
        
