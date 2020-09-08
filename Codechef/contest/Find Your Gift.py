# Find Your Gift :

for _ in range(int(input())):
    n = int(input())
    s = input()
    x=y=i=0
    while i<n-1:
        if s[i] == 'L':
            x -=1
            while(s[i]=='L' or s[i]=='R'):
                i+=1
            i-=1
        elif s[i] == 'R':
            x+=1
            while(s[i]=='L' or s[i]=='R'):
                i+=1
            i-=1
        elif s[i] == 'U':
            y+=1
            while(s[i]=='U' or s[i]=='D'):
                i+=1
            i-=1
        elif s[i] == 'D':
            y-=1
            while(s[i]=='U' or s[i]=='D'):
                i+=1
            i-=1
        i+=1
    print(x,y)
