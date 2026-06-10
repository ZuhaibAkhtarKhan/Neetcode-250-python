class MyHashSet(object):

    def __init__(self):
        self.arr = set()

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        self.arr.add(key)
        

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        if key in self.arr:
            self.arr.remove(key)
        

    def contains(self, key):
        """
        :type key: int
        :rtype: bool
        """
        return key in self.arr
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)