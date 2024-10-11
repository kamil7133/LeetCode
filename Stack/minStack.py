class MinStack:

    def __init__(self):
        self.main_stack = []
        self.min_stack = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.main_stack.append(val)

        if len(self.min_stack) == 0 or val <= self.min_stack[-1]:
            self.min_stack.append(val)


    def pop(self):
        """
        :rtype: None
        """
        if len(self.main_stack) == 0:
            return None
        val = self.main_stack.pop()
        if val == self.min_stack[-1]:
            self.min_stack.pop()


    def top(self):
        """
        :rtype: int
        """
        if len(self.main_stack) == 0:
            return None
        else:
            return self.main_stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        if len(self.min_stack) == 0:
            return None

        return self.min_stack[-1]
# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

#test
obj = MinStack()

obj.push(-2)
obj.push(0)
obj.push(-3)
param_1 = obj.getMin()
print("getMin:", param_1)

obj.pop()
param_2 = obj.top()
print("top:", param_2)
param_3 = obj.getMin()
print("getMin:", param_3)