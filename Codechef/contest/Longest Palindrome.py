# Longest Palindrome :

n = int(input())
s = input()

for i in range(n):
    for j in range(1,n+1):
        for k in range(i,i+j):
            if i+j < n:
                print(s[i+j],end='')
        print()




'''
def ispalindrome(s):
    for i in range(len(s)//2):
        if s[i] != s[-1-i]:
            return None
    return len(s)

ma = 0

for i in range(n): 
    for j in range(i+1,n+1): 
        data = s[i: j]
        val = ispalindrome(data)
        if val:
            if val > ma:
                ma = val
    print(ma)
'''
