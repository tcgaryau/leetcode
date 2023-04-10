# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        old_to_new_map = {}

        def dfs(node):
            if node in old_to_new_map:
                return old_to_new_map[node]

            copy = Node(node.val)
            old_to_new_map[node] = copy

            for neighbor in node.neighbors:
                copy.neighbors.append(dfs(neighbor))

            return copy

        return dfs(node) if node else None


def test_1_creation():
    node_1 = Node(1)
    node_2 = Node(2)
    node_3 = Node(3)
    node_4 = Node(4)
    node_1.neighbors = [node_2, node_4]
    node_2.neighbors = [node_1, node_3]
    node_3.neighbors = [node_2, node_4]
    node_4.neighbors = [node_1, node_3]
    return node_1


def test_2_creation():
    return Node(1)


def main():
    sol = Solution()
    test_1 = test_1_creation()
    test_2 = test_2_creation()
    test_3 = None  # same memory address at this point since it will be None

    for test in [test_1, test_2, test_3]:
        print(
            f"Original Node: {hex(id(test))}")
        clone = sol.cloneGraph(test)
        print(
            f"Copied Node: {hex(id(clone))}")


if __name__ == "__main__":
    main()
