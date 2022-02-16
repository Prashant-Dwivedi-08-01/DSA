# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

"""
The Recurisive approach of traversing a linked is really handy when
we have the need of keeping the track of previous node in linkedlis.

This is because, since we dont have backward pointer i.e it is not the
doubly linked list, then going back in the list becomes complicated and
we are forced to keep the track of the preivous nodes.

In such situation recursive traversing becomes handy because then once,
the recurisver call returns then we will be on the previous node by default.

Syntax
def travers(head):
    if head.next == None:
        print("We are on last node")
        return or do whatever want to do
    solve(head.next)

"""

#! Here the logic is simple
"""
1 -> 2-> 3-> 4->5 ->None

a. When I am on last node, set head as that node and return that node 
   to previous call
b. When on any node let say 4, then the call on 4 return 5th node to it.
    Here the next of 5th node is set to present 4th node and the next of 
    present 4th node is set to None ( this None of 4 is update in call for 3rd
    node, as 4 is returned there and so on....Thus on node 1 we set the next of 1
    as none, which becomes our tail)
"""

class Solution:
    head = None
    def reverseList(self, head):
        Solution.head = head
        if Solution.head == None:
            return Solution.head
        
        temp = Solution.head
        self.solve(temp)
        return Solution.head
    
    def solve(self, t):
        if t.next == None:
            Solution.head = t
            return t
        temp = self.solve(t.next)
        temp.next = t
        t.next = None
        return t