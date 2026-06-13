class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        h = len(nums) - 1
        l = 0
        while(l <= h):
            
            mid = int((l+h)/2)
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                h = mid - 1

        return -1
            