# Chef and Notebooks :--
def work(x,y,k,n,p,c):
    for i in range(n):
        if x-y <= p[i] and c[i] <= k:
            return "LuckyChef"
            
        return "UnluckyChef"



for _ in range(int(input())):
    x,y,k,n = map(int,input().split())
    p = list(map(int,input().split()))
    c = list(map(int,input().split()))
    print(work(x,y,k,n,p,c))

