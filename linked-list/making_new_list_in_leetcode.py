class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

head = None
temp = head
n = 5 # length on list
while n>0:
    node = ListNode(10)
    if head == None:
        temp = node
        head = node
    else:
        temp.next = node
        temp = node
    n -= 1

head # is the head of the new list