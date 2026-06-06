class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_map = {}

        for i in nums:
            if i in nums_map:
                nums_map[i] += 1
            else:
                nums_map[i] = 1

        return max(nums_map, key=nums_map.get)