# ballons :--

for _ in range(int(input())):
    n = int(input())
    if n%2 == 0:
        x = n//2
        print((x * (x +1)) //2)
    else:
        x = n//2 + 1
        print((x*(x+1)) // 2)
