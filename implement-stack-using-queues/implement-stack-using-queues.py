class MyStack(object):

    def __init__(self):
        self.q = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.q.append(x)
        

    def pop(self):
        """
        :rtype: int
        """
        
        i = 0
        while i < len(self.q) - 1:
            self.q.append(self.q.pop(0))
            i+=1
        
        return self.q.pop(0)

    def top(self):
        """
        :rtype: int
        """
        i = 0
        while i < len(self.q) - 1:
            self.q.append(self.q.pop(0))
            i+=1
        
        e = self.q.pop(0)
        self.q.append(e)
        return e

    def empty(self):
        """
        :rtype: bool
        """
        if not self.q:
            return True
        else:
            return False


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()