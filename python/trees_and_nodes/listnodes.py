class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = ListNode(0)
        result_tail = result
        carry = 0

        while l1 or l2 or carry:
            val1 = (l1.val if l1 else 0)
            val2 = (l2.val if l2 else 0)
            carry, out = divmod(val1 + val2 + carry, 10)

            result_tail.next = ListNode(out)        #create new node and assign it to current node next
            result_tail = result_tail.next          #advance current node to next

            l1 = (l1.next if l1 else None)          #get next node from lists
            l2 = (l2.next if l2 else None)

        return result.next

# [2,4,3]
# [5,6,4]
a = Solution(0)
l1 = ListNode(2)
l1_2 = ListNode(4)
l1_3 = ListNode(3)
l1.next = l1_2
l1_2.next = l1_3
l2 = ListNode(5)
l2_2 = ListNode(6)
l2_3 = ListNode(4)
l2.next = l2_2
l2_2.next = l2_3
b = a.addTwoNumbers(l1,l2)
print(b)