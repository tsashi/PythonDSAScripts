# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        curr = head
        i = 0
        l = []
        while curr is not None:
            l.append(curr.val)
            curr = curr.next
            i +=1
        n = i
        i = 0
        max = 0
        while i<(n/2):
            if max < l[i]+l[n-1-i]:
                max = l[i]+l[n-1-i]
            i +=1
        return max