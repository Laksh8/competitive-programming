# ATM

wd ,cb = map(int,input().split())

if wd<cb:
    if wd % 5 == 0:
        cb = cb-wd-0.5
        print("%.2f"%cb)
    else:
        print("%.2f"%cb)
else:
    print("%.2f"%cb)
