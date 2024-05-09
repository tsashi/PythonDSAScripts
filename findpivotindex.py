class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        n = len(nums)
        rights = sum(nums)
        lefts=0
        rights -= nums[0]
        if rights==lefts:
            return 0
        for i in range(1,n):
            lefts += nums[i-1]
            rights -= nums[i]
            if lefts == rights:
                return i
            if i==n-1 and rights==0 and lefts==0:
                return i
        return -1
    
myobj = Solution()
nums = [1,7,3,6,5,6,2,3,4,-2,-5,6,-1,3,4,-1,9]
print(myobj.pivotIndex(nums))
