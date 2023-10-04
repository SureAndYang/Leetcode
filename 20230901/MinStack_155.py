#!/usr/bin/python3

""" Medium: Min Stack
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:
    MinStack() initializes the stack object.
    void push(int val) pushes the element val onto the stack.
    void pop() removes the element on the top of the stack.
    int top() gets the top element of the stack.
    int getMin() retrieves the minimum element in the stack.
You must implement a solution with O(1) time complexity for each function.


"""

"""What I should remember is that the problem requires you can return the minimum in O(1) time, but
doesn't require the output of 'pop()' is the minimum.

Runtime 97.66%, Memory 64.25%.
"""
class MinStack:

    def __init__(self):
        self.stack = []
        self.min_pos = []


    def push(self, val: int) -> None:
        if not self.stack:
            self.min_pos.append(0)
        else:
            self.min_pos.append(
                    self.min_pos[-1] if self.stack[self.min_pos[-1]] < val else len(self.stack))
        self.stack.append(val)


    def pop(self) -> None:
        self.min_pos.pop()
        return self.stack.pop()


    def top(self) -> int:
        return self.stack[-1]


    def getMin(self) -> int:
        return self.stack[self.min_pos[-1]]



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
