import heapq
class Solution:
    def totalCost(self, costs: list[int], k: int, candidates: int) -> int:
        # n = len(costs)

        # left =0
        # right = n-1

        # leftqueue = []
        # rightqueue = []

        # totcost = 0

        # while k>0:
        #     while len(leftqueue) < candidates and left <= right:
        #         heapq.heappush(leftqueue, costs[left])
        #         left +=1
        #     while len(rightqueue) < candidates and left <= right:
        #         heapq.heappush(rightqueue, costs[right])
        #         right -= 1
        #     cost1 = leftqueue[0] if leftqueue else float('inf')
        #     cost2 =  rightqueue[0] if rightqueue else float('inf')
        #     if cost1 <= cost2:
        #         totcost += cost1
        #         heapq.heappop(leftqueue)
        #     else:
        #         totcost += cost2
        #         heapq.heappop(rightqueue)
        #     k -= 1
        # return totcost

        #single priority queue
        totcost = 0
        left, right = 0, len(costs) - 1
        pq = []
        heapq.heapify(pq)

        for _ in range(candidates):
            heapq.heappush(pq, [costs[left], 0])
            left += 1

        for _ in range(candidates):
            if left <= right:
                heapq.heappush(pq, [costs[right], 1])
                right -= 1

        while k > 0 and pq:
            curr = heapq.heappop(pq)
            totcost += curr[0]

            if left <= right:
                if curr[1] == 0:
                    heapq.heappush(pq, [costs[left], 0])
                    left += 1
                else:
                    heapq.heappush(pq, [costs[right], 1])
                    right -= 1

            k -= 1

        return totcost