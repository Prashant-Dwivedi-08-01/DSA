class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverse(self, head):
        curr = head
        prev = nxt = None
        while curr != None:
            # --> first fix next using curr node
            # --> then point curr node to back node 
            # --> then make present node as back(prev node) for next pass
            nxt = curr.next
            curr.next = prev
            prev = curr

            # updated current, i.e move ahead
            curr = nxt
        return prev

head = ListNode(1)
temp = head

temp.next = ListNode(2)
temp = temp.next

temp.next = ListNode(3)
temp = temp.next

temp.next = ListNode(4)
temp = temp.next

sol = Solution()
lst = sol.reverse(head)
while(lst != None):
    print(lst.val)
    lst = lst.next