class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1
        else:
            minus3 = 0
            minus2 = 1
            minus1 = 1
            for i in range(3,n+1):
                curr = minus1+minus2+minus3
                minus1, minus2, minus3 = curr, minus1, minus2
            return curr