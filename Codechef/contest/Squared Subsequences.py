# Squared Subsequences :--



def subSequence(lst,n):
    count = 0 
    for i in range(n):
        val = 1
        for j in range(i,n):
            val *=lst[j] 
            if (val)%4 != 2:
                count +=1
    return count


for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    print(subSequence(a,n))


'''
def subSequence(lst,n):
    count = 0 
    for i in range(n):
        for j in range(i,n):
            val = 1
            for k in range(i,j+1):
                val *= lst[k]
            if (val)%4 != 2:
                count +=1
    return count


for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    print(subSequence(a,n))
'''
