"""
2019/2/17
hsvnlu
time: 44ms 58.43%
space: 6.9MB 18.89%
"""
import queue
class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q = queue.Queue()

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        self.q.put(x)

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        l = self.q.qsize()
        for i in range(l - 1): self.q.put(self.q.get())
        return self.q.get()

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        l = self.q.qsize()
        for i in range(l - 1): self.q.put(self.q.get())
        t = self.q.get()
        self.q.put(t)
        return t

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return self.q.empty()


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
