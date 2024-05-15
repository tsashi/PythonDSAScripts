# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd = head
        if not odd:
            return None
        even = head.next
        evenhead = even
        # print(f"odd = {odd}, even = {even}")
        if not odd.next:
            return odd
        elif not even.next:
            return odd
        elif not even.next.next:
            odd.next = odd.next.next
            odd.next.next = even
            even.next = None
            print(odd)
            return head
        i = 0
        while odd.next and even.next:
            # print(f"i = {i}, odd = {odd}, even = {even}")
            odd.next = odd.next.next
            even.next = even.next.next
            odd = odd.next
            even = even.next
            # print(f"i = {i}, odd = {odd}, even = {even}")
            i +=1
        odd.next = evenhead
        # print(f"odd = {odd}, even = {even}")
        
        return head