class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        # nums = [0,1,2,2,3,0,4,2]
        # val = 2
        l = len(nums)
        k = 0
        for i in range(l):
            if nums[i] != val:
                nums[k] = nums[i]
                k+=1
                
        return k
        # print(l)
        # print(nums)

