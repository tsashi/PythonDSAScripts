from collections import Counter
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        snt = Counter(senate)
        while snt['D']>0 and snt['R']>0:
            n = len(senate)
            i = 0
            while i<n:
                if senate[i] == 'R':
                    if snt['D']>0:
                        if senate[i:].find('D') != -1:
                            senate = senate[:(i+senate[i:].find('D'))] + senate[(i+1+senate[i:].find('D')):]
                            i +=1
                        else:
                            senate = senate.replace('D','',1)
                        snt['D'] -=1
                        n -= 1
                    else:
                        return "Radiant"
                elif senate[i] == 'D':
                    if snt['R']>0:
                        if senate[i:].find('R') != -1:
                            senate = senate[:(i+senate[i:].find('R'))] + senate[(i+1+senate[i:].find('R')):]
                            i +=1
                        else:
                            senate = senate.replace('R','',1)
                        snt['R'] -=1
                        n -= 1
                    else:
                        return "Dire"
        if snt['D']==0:
            return "Radiant"
        else:
            return "Dire"
myobj = Solution()
senate = "DRRDRDRDRDDRDRDR"
print(myobj.predictPartyVictory(senate))
