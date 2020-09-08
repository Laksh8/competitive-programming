# Anagrams : 

for _ in range(int(input())):
    s1 = list(map(str,input().lower()))
    s2 = list(map(str,input().lower()))
    if set(s1) == set(s2) and len(s1) == len(s2):
        lst = list(s1)
        x = True
        for i in lst:
            if s1.count(i) != s2.count(i):
                x = False
                break
        
        if x:
            print("ANAGRAMS")
        else:
            print("NOT ANAGRAMS")
    else:
        print("NOT ANAGRAMS")
