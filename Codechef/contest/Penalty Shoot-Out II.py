# Penalty Shoot-Out II :--

def check(n,lst):
    a = 0
    b = 0
    for i in range(len(lst)):
        if i%2==0 and lst[i] == '1':
            a+=1
        elif lst[i] == '1':
            b+=1
        if a> n-i//2+b:
            return i
        elif b>n-i//2+a:
            return i
        
    return 2*n

for _ in range(int(input())):
    n = int(input())
    lst = input()
    print(check(n,lst))
        
        
