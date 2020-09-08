# The Way to a Friends House Is Never Too Long :
if __name__ == '__main__':
    TC = int(input())
    for _ in range(TC):
        line = input()
        N = int(input())
        arr = []
        for _ in range(N):
            input()
            x, y = list(map(int, input().split()))
            arr.append((x, y))
        arr.sort(key=lambda a: (a[0], a[1] * -1))
        dist = 0
        for i in range(1, N):
            x1 = arr[i][0]
            y1 = arr[i][1]
            x2 = arr[i-1][0]
            y2 = arr[i-1][1]
            d = ((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)) ** 0.5
            dist += d

        print("{:0.2f}".format(dist))

'''
def distance(x1,y1,x2,y2):
    return ((x2-x1)**2 + (y2-y1)**2)**(1/2)

def select(lst):
    start = lst[-1]
    end = lst[0]

    for i in lst:
        if i[0] == end[0] and i[1] <= end[1]:
            end = i
        else:
            return start,end
        
    

for _ in range(int(input())):
    input()
    n = int(input())
    lst = []
    for i in range(n):
        lst.append(list(map(int,input().split())))
    lst.sort(reverse=True)
    start,end = select(lst)
    if lst.index(start)>lst.index(end):
        start,end = end,start
    lst = lst[lst.index(start):lst.index(end)+1]
    dis = 0
    for i in range(1,len(lst)):
        dis = dis+distance(lst[i-1][0],lst[i-1][1],lst[i][0],lst[i][1])
    print('%.2f'%dis)         
'''



