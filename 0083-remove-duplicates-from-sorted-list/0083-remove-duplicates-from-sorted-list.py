# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next ==None:
            return head
        team = head
        while team.next != None:
            if team.val == team.next.val:
                team.next = team.next.next
            else:
                team = team.next
        return head
        
        
        
        
        
        
        
        
        
        
        
        
        
        # cur=head
     
        # if head is None:
        #   return head
        #   else:
        #     while cur.next!=None:
        #         if cur.val== cur.next.val:
        #           cur.next=cur.next.next
        #         else:
        #            cur=cur.next
        #     return head   