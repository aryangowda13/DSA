class MinStack:
# min_stack is used to keep track of the minimum value at each level of the stack
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val):
        self.stack.append(val)

        if not self.min_stack:
            self.min_stack.append(val)
        else:
            self.min_stack.append(min(val, self.min_stack[-1]))

    def pop(self):
        self.stack.pop()
        self.min_stack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.min_stack[-1]


# Input is already given
minStack = MinStack()

minStack.push(-1)
minStack.push(0)
minStack.push(2)

print("Minimum:", minStack.getMin())

minStack.pop()

print("Top:", minStack.top())
print("Minimum:", minStack.getMin())