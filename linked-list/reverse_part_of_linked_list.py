
# Definition for singly-linked list.
#! Leetcode
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head, left: int, right: int):
        first = None
        second = head
        i = 1
        while i < left:
            second = second.next
            if first == None:
                first = head
            else:
                first = first.next
            i += 1
        curr = second
        prev = nxt = None
        i = 1
        while i <= right-left+1: 
            nxt = curr.next
            curr.next = prev
            prev = curr

            curr = nxt
            i += 1
        
        second.next = curr
        if first == None:
            return prev
        first.next = prev
        return head