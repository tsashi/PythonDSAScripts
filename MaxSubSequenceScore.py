from itertools import combinations
# import numpy as np
class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        # n = len(nums1)
        # max = 0
        # for combo in combinations(range(n),k):
        #     sum = 0
        #     min = 10**5+1
        #     sum = 
        #     for i in combo:
        #         sum += nums1[i]
        #         if min>nums2[i]:
        #             min = nums2[i]
        #     temp = sum*min
        #     if max<temp:
        #         max = temp
        # return max
        
        # sumnums1comb = [sum(x) for x in list(combinations(nums1,k))]
        # minnums2comb = [min(x) for x in list(combinations(nums2,k))]
        # res_list = np.multiply(sumnums1comb,minnums2comb)
        # return max(res_list)

        maxres, prefixSum, minHeap = 0, 0, []
        
        for n1, n2 in sorted(list(zip(nums1, nums2)), key=itemgetter(1), reverse=True):
            prefixSum += n1
            heappush(minHeap, n1)
            if len(minHeap) == k:
                maxres = max(maxres, prefixSum * n2)
                prefixSum -= heappop(minHeap)                               
        
        return maxres