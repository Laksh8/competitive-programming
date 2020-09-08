# Circular Queue....

class CircularQueue:
    start = 0
    end = 1
    queue = ['None']*5
    def __init__(self,data):
        self.queue[0] = data
        
    def enqueue(self,data):
        if self.end != self.start:
            self.queue[self.end] = data
            self.end = (self.end +1)%5
        else:
            print("Queue is Full...")

    def dequeue(self):
        if self.start == self.end:
            print("Queue is Empty...")
        else:
            self.queue[self.start]='None'
            self.start+=1

    def peek(self):
       print(self.queue[self.start])

    def display(self):
        temp = self.start
        for i in range(len(self.queue)):
            if self.queue[i] != 'None':
                print(self.queue[(temp)%5])
            temp +=1


obj = CircularQueue(int(input("Enter Element :--")))
for i in range(2):
    obj.enqueue(int(input("Enter Element :--")))

obj.dequeue()
obj.peek()
obj.display()
for i in range(3):
    obj.enqueue(int(input("Enter Element :--")))
obj.display()

