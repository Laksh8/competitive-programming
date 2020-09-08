# Reversing directions : 

for _ in range(int(input())):
    n = int(input())
    lst = []
    for n in range(n):
        lst.append(list(input().split()))
    x = lst[-1][0]
    lst.reverse()
    for i in range(n):

        if i != 0:
            if val=='Left':
                lst[i][0] = 'Right'
                val = lst[i+1][0]
                
            else:
                lst[i][0]='Left'
                val = lst[i+1][0]
        else:
            val = lst[i][0]
            lst[i][0] = 'Begin'
    if x == "Left":
        lst[-1][0] = 'Right'
    else:
        lst[-1][0] = 'Left'
    print(lst)            
                
