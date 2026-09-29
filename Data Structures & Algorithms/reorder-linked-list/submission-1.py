# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
        # use slow fast pointers to get halfway into list, 
        # reorder from fast to slow
        # then do start, n -
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        prev = None
        node = slow.next
        slow.next = None
        while node:
            temp = node.next
            node.next = prev
            prev = node
            node = temp
        
        start, mid = head, prev
        while mid:
            next_start = start.next
            start.next = mid
            mid_next = mid.next
            mid.next = next_start
            start = next_start
            mid = mid_next
    
