class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        A = bin(a)[2:].zfill(30)
        B = bin(b)[2:].zfill(30)
        C = bin(c)[2:].zfill(30)

        res = 0
        for i in range(len(A)):
            if A[i] == '0' and B[i] == '0' and C[i] == '1':
                res += 1
            elif A[i] == '0' and B[i] == '1' and C[i] == '0':
                res += 1
            elif A[i] == '1' and B[i] == '0' and C[i] == '0':
                res += 1 
            elif A[i] == '1' and B[i] == '1' and C[i] == '0':
                res += 2
        return res

        # with bitwise operators
        # flips = 0
        # while a > 0 or b > 0 or c > 0:
        #     bit_a = a & 1
        #     bit_b = b & 1
        #     bit_c = c & 1

        #     if bit_c == 0:
        #         flips += (bit_a + bit_b)  
        #     else:
        #         if bit_a == 0 and bit_b == 0:
        #             flips += 1  

        #     a >>= 1
        #     b >>= 1
        #     c >>= 1

        # return flips