from typing import List
import unittest

class MinStack:

    def __init__(self):
        self.minStack = []
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)  
        if not self.minStack or val < self.minStack[-1]:  
            self.minStack.append(val)  
        else:  
            self.minStack.append(self.minStack[-1])  


    def pop(self) -> None:
        self.stack.pop()      
        self.minStack.pop() 


    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minStack[-1]



class test_MinStack(unittest.TestCase):
    def test_MinStack_1(self):
        obj = MinStack()
        obj.push(-2)
        obj.push(0)
        obj.push(-3)
        obj.getMin()
        obj.pop()
        param_3 = obj.top()
        param_4 = obj.getMin()
        self.assertEqual( 0 , param_3)

if __name__ == '__main__':
    unittest.main()