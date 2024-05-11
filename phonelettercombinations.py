class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        digstr = {'0':'', '1':'', '2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}

        outstr = []
        if digits == "":
            return outstr

        def combine(curlist:list[str], ch:str)->list[str]:
            if len(curlist)==0:
                return[var1 for var1 in ch]
            elif len(ch)==0:
                return curlist
            else:
                return [var1+var2 for var1 in curlist for var2 in ch]

        for ind, c in enumerate(digits):
            outstr = combine(outstr,digstr[c])
        
        return outstr

        # also interesting to use product func from itertools, see below:
        # from itertools import product
        # ch = [digstr[d] for d in digits]
        # return ["".join(var) for var in product(*ch)]

myobj = Solution()
digits = '4567'
print(myobj.letterCombinations(digits))