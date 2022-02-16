# https://leetcode.com/problems/middle-of-the-linked-list/submissions/

# Here slow is moving 1 step and fast is moving 2 steps thus when fast reaches end,
# slow would be int the middle
class Solution:
    def middleNode(self, head):
        slow = head
        fast = head
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
        return slow