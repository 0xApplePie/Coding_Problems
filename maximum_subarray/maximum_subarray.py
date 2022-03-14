class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr = max_arr = nums[0]
        for num in nums[1:]:
            curr = max(num, curr + num)
            max_arr = max(max_arr, curr)
        
        return max_arr