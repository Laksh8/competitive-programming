# Palindromic String

def check(s):
    for i in range(len(s)//2):
        if s[i] != s[-1-i]:
            return False
    return True


s =input()

if check(s):
    print('YES')
else:
    print('NO')
        
