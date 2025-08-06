class MyCircularQueue(object):

    def __init__(self, k):
        self.queue = [0] * k
        self.capacity = k
        self.head = 0
        self.count = 0
        """
        :type k: int
        """
        

    def enQueue(self, value):
        if self.count == self.capacity:
            return False
        self.queue[(self.head + self.count) % self.capacity] = value
        self.count += 1
        return True
        """
        :type value: int
        :rtype: bool
        """
        

    def deQueue(self):
        if self.count == 0:
            return False
        self.head = (self.head + 1) % self.capacity
        self.count -= 1
        return True

        """
        :rtype: bool
        """
        

    def Front(self):
        if self.count == 0:
            return -1
        return self.queue[self.head]

        """
        :rtype: int
        """
        

    def Rear(self):
        if self.count == 0:
            return -1
        return self.queue[(self.head + self.count - 1) % self.capacity]

        """
        :rtype: int
        """
        

    def isEmpty(self):
        return self.count == 0

        """
        :rtype: bool
        """
        

    def isFull(self):
        return self.count == self.capacity
        """
        :rtype: bool
        """
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()