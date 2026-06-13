# from collections import deque

# class MyStack(object):

#     def __init__(self):
#         self.q = deque()

#     def push(self, x):
#         """
#         :type x: int
#         :rtype: None
#         """
#         self.q.append(x)
        

#     def pop(self):
#         """
#         :rtype: int
#         """
#         return self.q.pop()
        

#     def top(self):
#         """
#         :rtype: int
#         """
#         return self.q[-1]
        

#     def empty(self):
#         """
#         :rtype: bool
#         """
#         return len(self.q) == 0
        


# # Your MyStack object will be instantiated and called as such:
# # obj = MyStack()
# # obj.push(x)
# # param_2 = obj.pop()
# # param_3 = obj.top()
# # param_4 = obj.empty()

from collections import deque
class MyStack(object):

    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """

        self.q1.append(x)
        while self.q2:
            self.q1.appendleft(self.q2.pop())

        while self.q1:
            self.q2.appendleft(self.q1.pop())
        

    def pop(self):
        """
        :rtype: int
        """
        return self.q2.pop()
        

    def top(self):
        """
        :rtype: int
        """
        return self.q2[-1]
        

    def empty(self):
        """
        :rtype: bool
        """
        return not self.q2
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()