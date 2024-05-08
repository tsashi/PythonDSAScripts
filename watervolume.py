class Solution:
    def maxArea(self, height: list[int]) -> int:
        n = len(height)
        if n==2:
            return min(height[0],height[1])
        left = 0
        right = n-1
        maxarea = 0

        while left < right:
            currarea = (right-left)*min(height[left],height[right])
            maxarea = max(maxarea,currarea)

            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return maxarea

myobj = Solution()
height = [1,8,6,2,5,4,8,3,7]
print(myobj.maxArea(height))
