class myQueue:
    def __init__(self, n):
        self.n = n
        self.arr = [0] * n
        self.front = 0
        self.rear = 0
        self.currSize = 0 
        
    def isEmpty(self):
        return self.currSize == 0
        
    def isFull(self):
        return self.currSize == self.n
       
    def enqueue(self, x):
        if not self.isFull():
            self.arr[self.rear] = x
            # Wrap rear pointer to the beginning if it hits the end
            self.rear = (self.rear + 1) % self.n
            self.currSize += 1
    
    def dequeue(self):
        if self.isEmpty():
            return -1
        element = self.arr[self.front]
        # Wrap front pointer
        self.front = (self.front + 1) % self.n
        self.currSize -= 1
        return element
       
    def getFront(self):
        if self.isEmpty():
            return -1
        return self.arr[self.front]
        
    def getRear(self):
        if self.isEmpty():
            return -1
        # Calculate the index of the last inserted element
        last_idx = (self.rear - 1 + self.n) % self.n
        return self.arr[last_idx]
        
        
        