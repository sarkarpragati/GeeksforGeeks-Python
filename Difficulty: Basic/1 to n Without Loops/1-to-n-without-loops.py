class Solution:
    def printTillN(self, N):
    	#code here 
    	if N < 1:
            return
        
        # Recursive Call: Go deeper until we reach 1
        self.printTillN(N - 1)
        
        # Print after the recursive call to ensure ascending order
        print(N, end=" ")