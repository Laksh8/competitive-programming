# Nastya and Scoreboard :--

dic = { "1110111":0, "0010010":1, "1011101":2, "1011011":3, "0111010":4, "1101011":5, "1101111":6, "1010010":7, "1111111":8, "1111011":9}

n,k = map(int,input().split())
for i in range(n):
    if k <= 0:
        break
    s = input()
    try:
        if dic[s] != 0 and dic[s] != 2 and dic[s] != 6 and dic[s] != 8:
            for i in range(7):
                if i!= 4 and s[i] != 1:
                    k -=1
                
    except:
        pass
    
