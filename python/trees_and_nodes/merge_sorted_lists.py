# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = cur = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        cur.next = l1 or l2
        return dummy.next

a = Solution()
l1 = ListNode(1)
l1_2 = ListNode(2)
l1_3 = ListNode(4)
l1.next = l1_2
l1_2.next = l1_3
l2 = ListNode(1)
l2_2 = ListNode(3)
l2_3 = ListNode(4)
l2.next = l2_2
l2_2.next = l2_3
b = a.mergeTwoLists(l1, l2)
print(b.val)
