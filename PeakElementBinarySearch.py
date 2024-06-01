class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        low = 0
        high = n-1
        if n == 1:
            return 0
        while low <=high:
            mid = (low+high)// 2
            if mid == 0:
                if nums[mid]>nums[mid+1]:
                    return mid
                else:
                    low = mid+1 
            elif nums[mid]>nums[mid-1]:
                if mid == n-1:
                    return mid
                elif nums[mid]>nums[mid+1]:
                    return mid
                else:
                    low = mid+1
            else:
                high = mid-1

        # even simpler code 
        # n = len(nums)
        # low = 0
        # high = n-1
        # while low < high:
        #     mid = (low + high) // 2

        #     if nums[mid] > nums[mid + 1]:
        #         high = mid
        #     else:
        #         low = mid + 1
        # return low