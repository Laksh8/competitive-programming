# Power...

def po(n,m,x):
    if m<1:
        return 1
    else:
      return n * po(n,m-1)
print(po(2,8))
