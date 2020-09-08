# Candies :--

for _ in range(int(input())):
    n = int(input())
    k = 2
    while True:
        if n%(2**(k) - 1) == 0:
            print((n//(2**(k) - 1)))
            break
        k+=1
        
