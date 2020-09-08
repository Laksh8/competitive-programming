
def check(p1,q1,p2,q2,x1,x2,y):
    if x1 <= p1 and x2 >= p2 and q1 < q2 and q1<=y and q2>=y:
        return True
    elif x1 <= p1 and x2 >= p2 and q1 > q2 and q2<=y and q1>=y:
        return True
    return False
            

for _ in range(int(input())):
    n,q = map(int,input().split())
    a = list(map(int,input().split()))
    for __ in range(q):
        x1,x2,y = map(int,input().split())
        count = 0
        for i in range(n-1):
            if check(i+1,a[i],i+2,a[i+1],x1,x2,y):
                count += 1
        print(count)
            




'''
class Point:
    def __init__(self, x, y): 
        self.x = x 
        self.y = y 
  
def onSegment(p, q, r): 
    if ( (q.x <= max(p.x, r.x)) and (q.x >= min(p.x, r.x)) and 
           (q.y <= max(p.y, r.y)) and (q.y >= min(p.y, r.y))): 
        return True
    return False
  
def orientation(p, q, r): 
    val = (float(q.y - p.y) * (r.x - q.x)) - (float(q.x - p.x) * (r.y - q.y)) 
    if (val > 0): 
        return 1
    elif (val < 0): 
        return 2
    else: 
        return 0

def doIntersect(p1,q1,p2,q2): 
    o1 = orientation(p1, q1, p2) 
    o2 = orientation(p1, q1, q2) 
    o3 = orientation(p2, q2, p1) 
    o4 = orientation(p2, q2, q1) 

    if ((o1 != o2) and (o3 != o4)): 
        return True

    if ((o1 == 0) and onSegment(p1, p2, q1)): 
        return True
  
    if ((o2 == 0) and onSegment(p1, q2, q1)): 
        return True
  
    if ((o3 == 0) and onSegment(p2, p1, q2)): 
        return True
  
    if ((o4 == 0) and onSegment(p2, q1, q2)): 
        return True  
    return False


p1 = Point(3, 5) 
q1 = Point(4, 1) 
p2 = Point(2, 4) 
q2 = Point(4,4) 
if doIntersect(p1, q1, p2, q2): 
    print("Yes") 
else: 
    print("No") 
  
p1 = Point(2,3) 
q1 = Point(3, 5) 
p2 = Point(2, 4) 
q2 = Point(4, 4) 
  
if doIntersect(p1, q1, p2, q2): 
    print("Yes") 
else: 
    print("No")
'''

