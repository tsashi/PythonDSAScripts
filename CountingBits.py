class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(n+1):
            n = 0
            while i>0:
                n += i & 1
                i = i>>1
            res.append(n)
        return res