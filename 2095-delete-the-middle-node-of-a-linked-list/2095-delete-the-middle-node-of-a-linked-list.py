# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
       if head.next is None:
        return None
       slow = head
       fast = head.next.next

       while fast and fast.next:
         slow = slow.next
         fast = fast.next.next
       slow.next = slow.next.next
       return head
      
      
      
      
    #    slow=head
    #    fast=head.next.next
    #    while fast and fast.next:
    #     slow=slow.next
    #     fast=fast.next.next
    #    slow.next=slow.next.next
    #    return head         
       
       
       
       
       
       
       
       
       
       
       
       
       
       
        # if head.next is None:
        #     return None 
        # slow=fast= head
        # prev=None
        # while fast and fast.next:
        #     prev=slow
        #     fast=fast.next.next
        #     slow=slow.next
        # prev.next=prev.next.next
        # return head    
