# Vowel Recognition :

def subString(s):
    for i in range(len(s)):
        for j in range(1,i):
            print(s[i:j])



for _ in range(int(input())):
    s = input()
    subString(s)
