from LeetCode_Linked_List_Code import LL
class Solution:
    def reverse(self, head):
        curr = head
        prev = nxt = None
        pas = 0
        while curr != None:
            pas += 1
            # --> first fix next using curr node
            # --> then point curr node to back node 
            # --> then make present node as back(prev node) for next pass
            nxt = curr.next
            curr.next = prev
            prev = curr

            # updated current, i.e move ahead
            curr = nxt
        return prev

lst = LL()
lst.append(1)
lst.append(2)
lst.append(3)
lst.append(4)

sol = Solution()
lst.set_head(sol.reverse(lst.get_head()))

lst.display()
