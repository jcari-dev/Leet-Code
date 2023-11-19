from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ls1 = []
        ls2 = []
        node1 = l1
        while node1:
            ls1.append(node1.val)
            node1 = node1.next
        node2 = l2
        while node2:
            ls2.append(node2.val)
            node2 = node2.next
        ls1.reverse()
        ls2.reverse()
        result1 = 0
        for num in ls1:
            result1 = result1 * 10 + num
        result2 = 0
        for num in ls2:
            result2 = result2 * 10 + num
        final_sum = result1 + result2
        final_sum_list = reversed([int(x) for x in str(final_sum)])
        return ListNode._array_to_list_node(final_sum_list)
