# Fibonacci Series....
'''
def febonacci(n):
    if n<= 1:
        return n
    return febonacci(n-1)+ febonacci(n-2)
print(febonacci(10))
'''

lst = []
for i in range(int(input())):
    if i <= 1:
        lst.append(i)
    else:
        lst.append(lst[i-1]+lst[i-2])

print(str(lst)[1:-1])

    
        
