# At the Gates

for _ in range(int(input())):
    n,k = map(int,input().split())
    val = input().split()
    for i in range(k):
        if val[-1-i] == 'H':
            for j in range(len(val)-1-i):
                if val[j] == 'H':
                    val[j] = 'T'
                else:
                    val[j] = 'H'
    
        
    print(val[:-k].count("H"))

            
            
