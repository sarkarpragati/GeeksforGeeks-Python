'''
class Node:
    def __init__(self, data): 
        self.data = data
        self.next = None
'''

class Solution:
    def lengthOfLoop(self, head):
        slow = head
        fast = head
        
       
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            
            
            if slow == fast:
                return self.countNodes(slow)
        
        
        return 0
        
    def countNodes(self, n):
        res = 1
        temp = n
        
        while temp.next != n:
            res += 1
            temp = temp.next
        return res
        