class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) == 1:
            return 0
        elif len(cost) == 2:
            return min(cost[0],cost[1])
        else:
            # return min(self.minCostClimbingStairs(cost[:-1])+cost[-1], self.minCostClimbingStairs(cost[:-2])+cost[-2])
            mincost0 = 0
            mincost1 = 0

            for i in range(2,len(cost)+1):
                curr = min(mincost0+cost[i-2],mincost1+cost[i-1])
                mincost0, mincost1 = mincost1, curr
            return curr