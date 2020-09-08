n = int(input("Enter a Number :-- "))

patlu = 0
motu = 1
su = 0
for i in range(n):
    if i %2 ==0:
        patlu += 1
        su += patlu
        if su >= n:
            print("Patlu")
            break
    else:
        motu = 2* patlu
        su += motu
        if su>=n:
            print("Motu")
            break
