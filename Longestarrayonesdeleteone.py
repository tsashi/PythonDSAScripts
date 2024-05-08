class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)

        if sum(nums)==n:
            return n-1
        
        maxones = 0
        currones = 0
        currzero = 0
        firstindexofwindow = 0
        for i,num in enumerate(nums):
            if num==1:
                currones +=1
                if (i==n-1) and (currones>maxones):
                    maxones = currones
            else:
                if (currzero<1):
                    currzero +=1
                    #currones +=1
                    if (i==n-1) and (currones>maxones):
                        maxones = currones
                else:
                    if (currones>maxones):
                        maxones = currones
                    while (nums[firstindexofwindow]==1):
                        currones -= 1
                        firstindexofwindow +=1
                    firstindexofwindow +=1
        return maxones