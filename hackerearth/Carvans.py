# Carvans :--

for _ in range(int(input())):
    n = int(input())
    cars = list(map(int,input().split()))
    count = 1
    temp = 0
    for i in range(len(cars)):
        if cars[i] < cars[temp]:
            temp = i
            count +=1
        elif cars[i] == cars[temp]:
            if temp !=i:
                count+=1
    print(count)
