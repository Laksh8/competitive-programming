# Duration :

for _ in range(int(input())):
    sh,sm,eh,em = map(int,input().split())
    shm = (sh*60)+sm
    ehm = (eh*60)+em
    tol = ehm-shm
    print(tol//60,tol%60)
