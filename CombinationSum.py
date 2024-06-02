from itertools import combinations
class Solution:
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        num = [1,2,3,4,5,6,7,8,9]

        out = [i for i in list(combinations(num,k)) if sum(i)==n]

        return out