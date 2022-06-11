class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        def rob_house(nums):
            curr1, curr2 = 0, 0
            for house in nums:
                temp = curr1
                curr1 = max(curr2 + house, curr1)
                curr2 = temp
            return curr1
        
        return max(rob_house(nums[1:]) , rob_house(nums[:-1]) )