# Its Confidential :

def encrypt(s):
    mid = len(s)//2
    if mid == 0:
        return s
    if len(s)%2 == 0:
        return s[mid-1]+encrypt(s[:mid-1]) + encrypt(s[mid:])
    else:
        return s[mid]+encrypt(s[:mid]) + encrypt(s[mid+1:])

print(encrypt("abc"))
'''
def solve(s):
    mid = len(s)//2
    if(mid==0):
        return s
    if len(s) % 2 == 0:
        return s[mid-1]+solve(s[0:mid-1])+solve(s[mid :])
    else:
       
        return s[mid]+solve(s[0:mid])+solve(s[mid + 1:])
'''        
n = int(input())
 
for i in range(n):
    x = int(input())
    st = input()
    print(encrypt(st))
