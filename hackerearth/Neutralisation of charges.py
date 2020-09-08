# Neutralisation of charges

n = int(input())
s = list(map(str,input()))
lst = []

def charges(s,n):
    lst = []
    for i in range(n-1):
        if s[i] == s[i+1]:
            del(s[i]);del(s[i+1])
            return charges(s,len(s))
        else:
            lst.append(s[i])
    return lst

