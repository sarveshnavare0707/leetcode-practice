'''
Design a stack class that supports the push, pop, top, and getMin operations.

    MinStack() initializes the stack object.
    void push(int val) pushes the element val onto the stack.
    void pop() removes the element on the top of the stack.
    int top() gets the top element of the stack.
    int getMin() retrieves the minimum element in the stack.

Each function should run in O(1)O(1) time.
'''

# brute force

class MinStack1:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]

    def getMin(self) -> int:
        return min(self.stack)
    
# O(1) time complexity for all operations except getMin, which is O(n) time complexity.

class MinStack2:
    def __init__(self):
        self.stack = []
        self.min_stack = [] # use a second stack to keep track of the minimum values
        
    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)
    
    def pop(self) -> None:
        if not self.stack:
            return
        
        if self.stack[-1] == self.min_stack[-1]:
            self.min_stack.pop()
        self.stack.pop()
        
    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        
    def getMin(self) -> int:
        if self.min_stack:
            return self.min_stack[-1]


if __name__ == "__main__":
    min_stack = MinStack2()
    min_stack.push(3)
    min_stack.push(5)
    print(min_stack.getMin())  # Output: 3
    min_stack.push(2)
    min_stack.push(1)
    print(min_stack.getMin())  # Output: 1
    min_stack.pop()
    print(min_stack.getMin())  # Output: 2
    min_stack.pop()
    print(min_stack.top())      # Output: 5
    print(min_stack.getMin())   # Output: 3