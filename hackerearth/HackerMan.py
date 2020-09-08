# HackerMan :


t=int(input())
while(t>0):
    t=t-1
    a,b=input().split()
    a=a[::-1]
    b=b[::-1]
    r=str(int(a)+int(b))
    r=r[::-1]
    print(int(r))
'''
def reverse(a):
    temp = 0
    while a>0:
        temp = temp*10 + a%10
        a//=10
    return temp

for _ in range(int(input())):
    a,b = map(int,input().strip().split())
    ra = reverse(a)
    rb = reverse(b)
    temp = ""
    val = str(ra+rb)
    for i in range(len(val)-1,-1,-1):
        temp +=val[i]
    print(temp)
'''
