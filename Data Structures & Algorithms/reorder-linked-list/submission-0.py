class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
        
        slow = head
        fast = head
    
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Separate the two halves
        reverse_start = slow.next
        slow.next = None
        
        prev = None
        while reverse_start:
            temp = reverse_start.next
            reverse_start.next = prev
            prev = reverse_start
            reverse_start = temp
        
        second = prev
        first = head
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2