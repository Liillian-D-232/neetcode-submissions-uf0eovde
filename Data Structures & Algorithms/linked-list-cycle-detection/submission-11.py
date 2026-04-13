# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        temp = head
        mem = []
        while temp is not None:
            if temp.next is None:
                return False
            elif temp in mem:
                return True
            elif temp is None:
                return False
            mem.append(temp)
            temp = temp.next
        return False