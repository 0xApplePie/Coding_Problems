import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)
        for i in range(len(nums)):
            num = nums.pop(i)
            _ans = math.prod(nums)
            nums.insert(i,num)
            ans[i] = _ans
        return ans