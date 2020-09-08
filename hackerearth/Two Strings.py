# Two Strings
def check(s1,s2):
    val = list(set(s1))
    for i in val:
        if s1.count(i) != s2.count(i):
            return "No"
    return "Yes"



# Write your code here
for _ in range(int(input())):
    s1,s2 = input().split()
    print(check(s1,s2))
