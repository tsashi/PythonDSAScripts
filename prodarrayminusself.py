class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        import numpy as np
        tempnums = nums.copy()
        n = len(nums)
        result = np.prod(nums)
        resultlist = [result] * len(nums)
        for i in range(n):
            if nums[i] == 0:
                tempnums[i] = 1
                resultlist[i] = np.prod(tempnums)
                tempnums = nums
            else:
                resultlist[i] = resultlist[i]//nums[i]
        return resultlist
    
myobj = Solution()
nums = [0, 0]
print(myobj.productExceptSelf(nums))