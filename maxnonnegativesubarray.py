class Solution:
    # @param A : list of integers
    # @return a list of integers
    def maxset(self, A):
        n = len(A)
        maxsum = 0
        maxB = []
        maxlenB = 0
        if n<1:
            return maxB
        if (n==1):
            if (A[0]<0):
                return maxB
            else:
                return A
        currsum = 0
        currB = []
        currlenB = 0
        for i in range(n):
            if A[i]>=0:
                currB.append(A[i])
            else:
                currlenB = len(currB)
                if currlenB>=1:
                    currsum = sum(currB)
                    if currsum>maxsum:
                        maxsum = currsum
                        maxB = currB
                        maxlenB = currlenB
                    elif currsum == maxsum:
                        if maxlenB < currlenB:
                            maxB = currB
                            maxlenB = currlenB
                currsum = 0
                currB = []
                currlenB = 0
        currlenB = len(currB)
        if currlenB>=1:
            currsum = sum(currB)
            if currsum>maxsum:
                maxsum = currsum
                maxB = currB
                maxlenB = currlenB
            elif currsum == maxsum:
                if maxlenB < currlenB:
                    maxB = currB
                    maxlenB = currlenB
        return maxB                
    
myobj = Solution()
A = [-1, -1, -2, -9, 10, 15, -6, 7, 8, -9, 0, 1, -3, -30, -30, 7, 8, 10, 0, -1]
print(myobj.maxset(A))
