class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        n = len(s)

        ksum = 0
        if k==n:
            for i, letter in enumerate(s):
                if letter in 'aeiou':
                    ksum+=1
            return ksum
        else:
            prevsum = 0
            for i, letter in enumerate(s[:k]):
                if letter in 'aeiou':
                    prevsum+=1
                    if i==0:
                        prevletter = 1
                else:
                    if i==0:
                        prevletter = 0
            maxsum = prevsum

            for i in range(k,n):
                if s[i] in 'aeiou':
                    currletter = 1
                else:
                    currletter = 0
                currsum = prevsum-prevletter+currletter
                
                if currsum>maxsum:
                    maxsum = currsum
                prevsum = currsum

                if s[i-k+1] in 'aeiou':
                    prevletter = 1
                else:
                    prevletter = 0
            return maxsum
        
myobj = Solution()
s = "abciiidef"
print(myobj.maxVowels(s,3))


