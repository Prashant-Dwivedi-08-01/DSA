class ListNode:
    def __init__(self, val) -> None:
        self.val = val
        self.next = None
class LL:
    def __init__(self) -> None:
        self.head = None

    def get_head(self):
        return self.head
    def set_head(self, node):
        self.head = node
    def append(self, val):
        new_node = ListNode(val)
        temp = self.head
        if temp == None:
            self.head = new_node
        else:
            while temp.next != None:
                temp = temp.next
            temp.next = new_node
    
    def display(self):
        temp = self.head
        while temp != None:
            print(temp.val, end=" ")
            temp = temp.next
    
