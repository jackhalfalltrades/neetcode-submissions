# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None
        return self.mergesort(lists, 0, len(lists) - 1)
    def mergesort(self, lists, l, r):
        if l > r:
            return None
        if l == r:
            return lists[l]
        
        m = l + (r - l) // 2
        left = self.mergesort(lists, l, m)
        right = self.mergesort(lists, m+1, r)

        return self.merge(left, right)
        
    def merge(self, l1, l2):
        dummy = ListNode(0)
        curr = dummy
        while l1 and l2:
            if l1.val <= l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
            
        if l1:
            curr.next = l1            
        else:
            curr.next = l2

        return dummy.next