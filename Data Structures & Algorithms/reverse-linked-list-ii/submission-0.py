# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # want to get after right since that will be used whe reversing
        # then just reverse it
        # get everything before the start value
        dummy = ListNode(0)
        dummy.next = head
        before_left = dummy
        for i in range(1, left):
            before_left = before_left.next
        # go to right value and get the next val
        right_node = dummy
        for i in range(right):
            right_node = right_node.next
        after_right = right_node.next
        prev = after_right
        
        node  = before_left.next
        # reverse the values
        for i in range(right - left + 1):
            temp = node.next
            node.next = prev
            prev = node
            node = temp

        before_left.next = prev

        
        return dummy.next

