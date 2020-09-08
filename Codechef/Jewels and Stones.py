# Jewels and Stones


for _ in range(int(input())):
    j = input()
    s = input()
    count = 0
    for i in s:
        if i in j:
            count+=1
    print(count)
