# Question 1

n = int(input())

lst = sorted(list(map(int,input().split())))

temp = list(set(lst))

for i in range(temp):
    if lst.count(i) > n+1
