from typing import Optional
# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseListRecursion(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Time Complexity O(n)
        Space Complexity O(n) - from call stacks
        """
        def reverseHelper(curr, prev=None):
            if not curr:
                return prev
            temp = curr.next
            curr.next = prev
            return reverseHelper(temp, curr)
        return reverseHelper(head)

    def reverseListIterative(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Time Complexity O(n)
        Space Complexity O(1)
        """
        prev, curr = None, head
        while curr:
            temp = curr.next
            curr.next = prev
            prev, curr = curr, temp
        return prev
