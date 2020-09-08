# Reverse of String using Recursion

def reverse(s,k,val):
    if k>=0:
        val += s[k]
        return reverse(s,k-1,val)
    return val


s = input("Enter a String ")
k = len(s)-1

val = reverse(s,k,'')

print(val)
