class MyQueue(object):

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack1.append(x)
        

    def pop(self):
        """
        :rtype: int
        """
        i = 0
        length = len(self.stack1)-1
        while i < length:
            e = self.stack1.pop()
            self.stack2.append(e)
            i+=1
         
        result = self.stack1.pop()
        
        
        while self.stack2:
            e = self.stack2.pop()
            self.stack1.append(e)
            
        return result
        

    def peek(self):
        """
        :rtype: int
        """
        i = 0
        length = len(self.stack1)-1
        while i < length:
            e = self.stack1.pop()
            self.stack2.append(e)
            i+=1
         
        result = self.stack1.pop()
        self.stack2.append(result)
        
        while self.stack2:
            e = self.stack2.pop()
            self.stack1.append(e)
            
        return result

    def empty(self):
        """
        :rtype: bool
        """
        if not self.stack1:
            return True
        else:
            return False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()