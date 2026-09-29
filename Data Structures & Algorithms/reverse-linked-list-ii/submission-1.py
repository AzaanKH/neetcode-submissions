# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        before_left = dummy
        for i in range(1, left):
            before_left = before_left.next

        right_node = dummy
        for i in range(right):
            right_node = right_node.next
        prev = right_node.next
        start = before_left.next
        for i in range(right  - left + 1):
            temp = start.next
            start.next = prev
            prev = start
            start = temp
        
        before_left.next = prev
        return dummy.next
         
        