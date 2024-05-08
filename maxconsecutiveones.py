class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        n = len(nums)

        maxones = 0
        currk = 0
        currnum = 0
        firstnuminwindow = 0
        for i, num in enumerate(nums):
            if num==1:
                currnum +=1
                if (i==n-1) and (currnum>maxones):
                    maxones = currnum
            elif (num==0):
                if (currk<k):
                    currnum +=1
                    currk +=1
                    if (i==n-1) and (currnum>maxones):
                        maxones = currnum
                else:
                    if currnum>maxones:
                        maxones = currnum
                    while nums[firstnuminwindow]==1:
                        currnum -=1
                        firstnuminwindow += 1
                    firstnuminwindow +=1
        return maxones
    
myobj = Solution()
nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
print(myobj.longestOnes(nums, 3))