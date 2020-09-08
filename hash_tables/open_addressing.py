# Open Addressing
# h(k) = 2*k +3
# We are Using Linear Probing...

def has(m,num):
    arr = [None]*m
    for i in range(num):
        ele = int(input("Enter a Number :-- "))
        hk = (2*ele+3)%10
        if arr[hk] == None:
            arr[hk] = ele
        else:
            for j in range(m):
                hk= (hk+1)%m
                if arr[hk] == None:
                    arr[hk] = ele
                    break
    return arr

print(has(10,8))

                
