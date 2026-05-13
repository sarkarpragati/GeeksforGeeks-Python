'''
class Node:
    def __init__(self, x):
        self.data = x
        self.next = None
'''

class Solution:
    def insertPos(self, head, pos, val):
        new_node = Node(val)
        
        
        if pos == 1:
            new_node.next = head
            return new_node
        
        
        curr = head
        for _ in range(pos - 2):
            if curr is None:
                break
            curr = curr.next
        
        
        if curr:
            new_node.next = curr.next
            curr.next = new_node
            
        return head
     