# Ali and Helping innocent people :

val = list(map(str,input()))
if val[2] == 'A' or val[2] == 'E' or val[2] == 'I' or val[2] == 'O' or val[2] == 'U' or val[2] == 'Y':
    print("invalid")
else:
    del(val[2]);del(val[6])
    for i in range(len(val)-1):
        if int(val[i])+int(val[i+1]) % 2 == 0:
            print("valid")
        else:
            print("invalid")
            break
    
