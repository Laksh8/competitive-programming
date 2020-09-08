# ThunderCracker :--
'''
for _ in range(int(input())):
    a = input().split()
    b = input().split()

    h1 , m1 = map(int,a[0].split(":"))
    h2 , m2 = map(int,b[0].split(":"))
    count = 0
    if abs(m1-m2) >= 30:
        count +=60-abs(m1-m2)
    else:
        count += abs(m1-m2)

    if a[1] != b[1] or (h1 == 11 and a[1] == b[1]):
        count +=1
    
    count += abs(h1-h2)
    print(count)'''
lst = []
while True:
    try :
        lst.append(int(input()))
    except:
        break
