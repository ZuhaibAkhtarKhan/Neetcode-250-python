# class Solution(object):
#     def containsNearbyDuplicate(self, nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: bool
#         """
        
#         l = len(nums)
#         if l <= 1:
#             return False

#         for i in range(l-2):
#             for j in range(i+1, l - 1):
#                 if nums[i] == nums[j] and abs(i-j) <= k:
#                     return True
            
#         return False
    
     # TIME limit exceeded

# class Solution(object):
#     def containsNearbyDuplicate(self, nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: bool
#         """
#         l = len(nums)

#         i = 0

#         while(i < l - 2):
#             for j in range(i+1, i+k + 1):
#                 if nums[i] == nums[j]:
#                     return True
#             i+=1
        
#         return False

        # TIME LIMIT EXCEEDED AGAIN


class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        