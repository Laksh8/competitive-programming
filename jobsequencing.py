# Job Sequencing Problem :--

#Taking Values of deadlines and their coresponding Profites 
deadlines ,profits = list(map(int,input("Enter Deadlines :-- ").split())),list(map(int,input("Enter Profits :-- ").split()))

a,arr = 'b',[]

#converting in the format of list of (jobs,deadlines,profits)
for deadline,profit in zip(deadlines,profits):
    arr.append((chr(ord(a)-1),deadline,profit)) 
    a = chr(ord(a)+1)

#Sorting in the decreasing order of Profit
arr.sort(key=lambda x:x[2],reverse=True)

#Taking Number of Slots
lst,maxprofit = [-1]*max(deadlines),0

#Solution :-- 
for job,deadline,profit in arr:
    for j in range(deadline-1,-1,-1):
        if lst[j] ==-1:
            lst[j] = job
            maxprofit += profit
            break

print("Maximum Profite is {0} \nJob Sequence should be {1}".format(maxprofit,lst))
    
    
