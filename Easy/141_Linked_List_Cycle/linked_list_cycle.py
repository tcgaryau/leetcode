from typing import Optional

# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        This solution uses Floyd's cycle detection algorithm to detect if a cycle exists.
        Time Complexity O(n)
        Space Complexity O(1)
        """
        tortoise = head
        hare = head
        while hare and hare.next:
            tortoise = tortoise.next
            hare = hare.next.next
            if tortoise == hare:
                return True
        return False


def test_1(solution):
    head = ListNode(3)
    two_node = ListNode(2)
    zero_node = ListNode(0)
    four_node = ListNode(4)
    head.next = two_node
    two_node.next = zero_node
    zero_node.next = four_node
    four_node.next = two_node
    print(solution(head))


def test_2(solution):
    head = ListNode(1)
    two_node = ListNode(2)
    head.next = two_node
    two_node.next = head
    print(solution(head))


def test_3(solution):
    head = ListNode(1)
    print(solution(head))


def main():
    sol = Solution()
    test_1(sol.hasCycle)  # [3, 2, 0, -4], pos 1 -> True
    test_2(sol.hasCycle)  # [1, 2], pos 0 -> True
    test_3(sol.hasCycle)  # [1], pos -1 -> False


if __name__ == "__main__":
    main()
