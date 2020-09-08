testcase = int(input())
while testcase > 0:
    num = int(input())
    sum=0
    divisor=5
    while (num)>=5:
        num = num // divisor
        sum = sum + num
    print(sum)
    testcase = testcase - 1
