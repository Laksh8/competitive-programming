# Lift queries...

start = 0
end = 7
    
for _ in range(int(input())):
    n = int(input())
    if n-start <= end-n:
        print("A")
        start = n
    else:
        print("B")
        end = n
