from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        seen = set()
        current_node = head
        previous_node = None

        while current_node:
            if current_node.val in seen:
                previous_node.next = current_node.next
            else:
                seen.add(current_node.val)
                previous_node = current_node
            current_node = current_node.next

        return head
