# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

# Implement the MinStack class:

# MinStack() initializes the stack object.
# void push(int val) pushes the element val onto the stack.
# void pop() removes the element on the top of the stack.
# int top() gets the top element of the stack.
# int getMin() retrieves the minimum element in the stack.
# You must implement a solution with O(1) time complexity for each function.

class MinStack(object):

    def __init__(self,stack = None):
        if stack == None: 
            self.items = []
        else : self.items = list
        

    def push(self, val):
        self.items.append(val)        

    def pop(self):
        return self.items.pop()
        

    def top(self):
        return self.items[-1]
        

    def getMin(self):
        return min(self.items)

#Your MinStack object will be instantiated and called as such:
obj = MinStack()
val = 0
obj.push(0)
obj.pop()
param_3 = obj.top()
param_4 = obj.getMin()