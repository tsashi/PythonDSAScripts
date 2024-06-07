class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        #Hint Try dynamic programming. DP[i][j] represents the longest common subsequence of text1[0 ... i] & text2[0 ... j].
        #DP[i][j] = DP[i - 1][j - 1] + 1 , if text1[i] == text2[j] DP[i][j] = max(DP[i - 1][j], DP[i][j - 1]) , otherwise
        m = len(text1)
        n = len(text2)
        A = [[-1]*(m+1) for i in range(n+1)]

        for i in range(n,-1,-1):
            for j in range(m,-1,-1):
                if (i == n) or (j == m):
                    A[i][j]=0
                elif text1[j]==text2[i]:
                    A[i][j] = 1+A[i+1][j+1]
                else:
                    A[i][j] = max(A[i+1][j], A[i][j+1])
                    
        return A[0][0]

myobj = Solution()
text1 = 'abcde'
text2 = 'ace'
print(myobj.longestCommonSubsequence(text1,text2))