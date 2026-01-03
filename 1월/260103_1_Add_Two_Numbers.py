from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        answer = ListNode()
        current = answer
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            if l1: l1 = l1.next
            val2 = l2.val if l2 else 0
            if l2: l2 = l2.next

            sum = val1 + val2 + carry
            carry = sum // 10
            sum = sum % 10

            current.next = ListNode(sum)
            current = current.next
        
        return answer.next

linked_list = Solution()
l1 = ListNode(2, ListNode(4, ListNode(3)))
l2 = ListNode(5, ListNode(6, ListNode(4)))
result = linked_list.addTwoNumbers(l1, l2)

vals = []
while result:
    vals.append(result.val)
    result = result.next

print(vals)