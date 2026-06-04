class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        '''
        l = len(nums)
        for i in range(l-1):
            for j in range(i+1, l):
                if nums[i]+nums[j] == target:
                    return [i, j]
                '''
        
        hmap = {}

        for i, n in enumerate(nums):
            partner = target - n
            if partner in hmap:
                return hmap[partner], i
            hmap[n] = i

