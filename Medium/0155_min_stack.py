class MinStack:

    def __init__(self):
        self._min_stack = []
        self._stack = []

    def push(self, val: int) -> None:
        self._stack.append(val)
        if self._min_stack:
            val = min(self._min_stack[-1], val)
        self._min_stack.append(val)

    def pop(self) -> None:
        self._stack.pop()
        self._min_stack.pop()

    def top(self) -> int:
        return self._stack[-1]

    def getMin(self) -> int:
        return self._min_stack[-1]


def test():
    min_stack = MinStack()
    min_stack.push(-2)
    min_stack.push(0)
    min_stack.push(-3)
    assert (min_stack.getMin() == -3)
    min_stack.pop()
    assert (min_stack.top() == 0)
    assert (min_stack.getMin() == -2)


if __name__ == "__main__":
    test()
