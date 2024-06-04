class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        elif n == 2:
            return max(nums[0], nums[1])
        elif n == 3:
            return max(nums[0]+nums[2],nums[1])
        else:
            maxcost0= nums[0]
            maxcost1= nums[1]
            maxcost2= nums[0]+nums[2]
            for i in range(3,n):
                curr = max(maxcost0+nums[i],maxcost1+nums[i])
                maxcost0, maxcost1, maxcost2 = maxcost1, maxcost2, curr
            return max(maxcost1, curr)