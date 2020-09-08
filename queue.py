import numpy as np


class Queue:
    queue = np.zeros(10)
    start = end = 0
    def enqueue(self,data):
        self.queue[self.end] = data
        self.end+=1

    def dequeue(self):
        print("{} Will be deleted Now...".format(int(self.queue[self.start])))
        self.start +=1

    def peek(self):
        print(int(self.queue[self.start]))

    def display(self):
        for i in range(self.start,self.end):
            print(int(self.queue[i]))

obj = Queue()
obj.enqueue(int(input("Enter a Number :-- ")));obj.enqueue(int(input("Enter a Number :-- ")));obj.enqueue(int(input("Enter a Number :-- ")));obj.enqueue(int(input("Enter a Number :-- ")));obj.enqueue(int(input("Enter a Number :-- ")));obj.enqueue(int(input("Enter a Number :-- ")))
obj.dequeue();obj.peek();obj.enqueue(int(input("Enter a Number :-- ")));obj.display()
