class myStack:
    def __init__(self, n):
        self.n = n          # Max capacity
        self.stack = []
        # Define Data Structures

    
    def isEmpty(self):
        return len(self.stack) == 0
        # Check if stack is empty

    
    def isFull(self):
        # Check if stack is full
        return len(self.stack) == self.n

    
    def push(self, x):
        if not self.isFull():
            self.stack.append(x)
        # Insert x at the top of the stack

    
    def pop(self):
        if not self.isEmpty():
            self.stack.pop()
        # Removes an element from the top of the stack

    
    def peek(self):
        if self.isEmpty():
            return -1
        return self.stack[-1]
        # Returns the top element of the stack