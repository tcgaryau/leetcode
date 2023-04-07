from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return str(self.val)


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        I used floyd's cycle detection algorithm to determine if there is a cycle first. 
        Then another pointer is made which is incremented at the same speed as the fast pointer until
        they hit each other which will give the first node of the cycle.
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        def has_cycle(head):
            tortoise = head
            hare = head
            while hare and hare.next:
                tortoise = tortoise.next
                hare = hare.next.next
                if tortoise == hare:
                    return True, hare
            return False, None

        is_cycle, hare = has_cycle(head)

        if is_cycle:
            start = head

            while start != hare:
                start = start.next
                hare = hare.next
        return hare


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
    test_1(sol.detectCycle)  # [3, 2, 0, -4], pos 1 -> Node 2
    test_2(sol.detectCycle)  # [1, 2], pos 0 -> Node 1
    test_3(sol.detectCycle)  # [1], pos -1 -> None


if __name__ == "__main__":
    main()
