"""
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
"""

class Solution:
    def printList(self, head):
        if not head:
            return
        curr = head
        while curr:
            
            print(curr.data, end=" ")
            curr = curr.next
        
        
        