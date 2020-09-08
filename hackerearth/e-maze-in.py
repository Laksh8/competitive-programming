# e-maze-in

command = input()
x = [0,0]

for i in command:
    if i == 'L':
        x[1] -= 1
    elif i == 'R':
        x[1] += 1
    elif i == 'U':
        x[0] +=1
    else:
        x[0] -=1
print(f"{x[1]} {x[0]}")
