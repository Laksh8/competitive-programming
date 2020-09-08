# Hack the money...

def hack(n,c):
    if c == n:
        return "Yes"
    if c > n:
        return "No"
    if c<n:
        if c*20 <n:
            return hack(n,c*20)
        else:
            return hack(n,c*10)
        


for _ in range(int(input())):
    n = int(input())
    print(hack(n,1))

