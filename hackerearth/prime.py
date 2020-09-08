from sys import stdin,stdout

def solve(n):
    if n<=9:
        return n

    else:
        return n%9+10*solve(n//9)

'''for data in stdin:
    data = int(data.rstrip('\n'))
'''
print(stdin)

