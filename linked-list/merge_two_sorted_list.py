# Definition for singly-linked list.
# Leetcode Question from Kunal's Kushwaha's playlist
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1, list2):
        ans = None
        head = None
        while(list1 != None and list2 != None):
            newNode = ListNode()
            if list1.val > list2.val:
                newNode.val = list2.val
                list2 = list2.next
            else:
                newNode.val = list1.val
                list1 = list1.next
            if ans == None:
                ans = newNode
                head = ans
            else:
                ans.next = newNode
                ans = ans.next
    
        if list1 == None:
            while list2 != None:
                newNode = ListNode()
                newNode.val = list2.val
                list2 = list2.next
                if ans == None:
                    ans = newNode
                    head = ans
                else:
                    ans.next = newNode
                    ans = ans.next
        if list2 == None:
            while list1 != None:
                newNode = ListNode()
                newNode.val = list1.val
                list1 = list1.next
                if ans == None:
                    ans = newNode
                    head = ans
                else:
                    ans.next = newNode
                    ans = ans.next
        return head
