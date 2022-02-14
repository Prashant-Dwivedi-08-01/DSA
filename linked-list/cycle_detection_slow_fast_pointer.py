# Look at the image in images folder under the name Cycle Detection 1 and 2
# Leetcode Q: https://leetcode.com/problems/linked-list-cycle/submissions/

#! LOGIC: We have two pointers, one move one step, and other move 2 steps
#! Since both have different speeds they will meet if cycle is present otherwise
#! fast pointer will be the first to reach NONE

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head) -> bool:
        slow_pointer = fast_pointer = head
        while fast_pointer != None and fast_pointer.next != None:
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next
            
            if slow_pointer == fast_pointer:
                return True
        return False