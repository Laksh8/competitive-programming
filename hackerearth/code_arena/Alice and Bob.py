# Alice and Bob :-- 

for _ in range(int(input())):
    n = int(input())
    bob = sum(list(map(int,input().split())))
    alice = sum(list(map(int,input().split())))
    if alice > bob:
        print("Alice")
    elif bob > alice :
        print("Bob")
    else:
        print("Tie")
