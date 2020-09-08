# Monk Takes a Walk : 

for _ in range(int(input())):
    s = input().lower()
    count = s.count('a') + s.count('e') + s.count('i') + s.count('o') + s.count('u')
    print(count)
