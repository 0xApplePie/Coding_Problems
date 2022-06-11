class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head is None:
            return head
        
        prev = head
        curr = head.next
        
        while curr != None:
            if prev.val == curr.val:
                prev.next = curr.next 
            else:
                prev = prev.next
            curr = curr.next
        
        return head