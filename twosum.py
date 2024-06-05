class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        b = nums.copy()
        nums.sort()
        for ind, i in enumerate(nums):
            l = ind+1
            h = len(nums)-1
            f = target-i
            while l<=h:
                mid = (l+h)//2
                if nums[mid]<f:
                    l = mid+1
                elif nums[mid]>f:
                    h = mid-1
                else:
                    res = []
                    if nums[ind] != nums[mid]:
                        res.append(b.index(nums[ind]))
                        res.append(b.index(nums[mid]))
                    else:
                        res.append(b.index(nums[ind]))
                        b[b.index(nums[ind])] += 1
                        res.append(b.index(nums[mid]))
                    return res

        #Using Hash Table
        # hashmap = {}
        # for i in range(len(nums)):
        #     complement = target - nums[i]
        #     if complement in hashmap:
        #         return [i, hashmap[complement]]
        #     hashmap[nums[i]] = i
    

myobj = Solution()
nums = [3,3]
print(myobj.twoSum(nums,6))