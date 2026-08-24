class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(nums) <= 2: 
            if len == 1: return False
            if len == 2: return nums[0] == nums[1] 
        list = [None for i in range(9)]