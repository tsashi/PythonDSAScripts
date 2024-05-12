import time
from collections import Counter
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        print("1.--- %s seconds ---" % (time.time() - start_time))
        # word1freq = {x: word1.count(x) for x in word1}
        # word2freq = {x: word2.count(x) for x in word2}
        word1freq = Counter(word1)
        word2freq = Counter(word2)
        print("2.--- %s seconds ---" % (time.time() - start_time))
        
        word1charset = set(word1freq.keys())
        word2charset = set(word2freq.keys())
        print("3.--- %s seconds ---" % (time.time() - start_time))
        if (word1charset != word2charset):
            return False
        print("4.--- %s seconds ---" % (time.time() - start_time))
        sortedfreq1 = sorted(word1freq.values())
        sortedfreq2 = sorted(word2freq.values())
        print("5.--- %s seconds ---" % (time.time() - start_time))
        if sortedfreq1 != sortedfreq2:
            return False
        
        return True
    
myobj = Solution()
start_time = time.time()
word1 = "abc"
word2 = "bca"
print(myobj.closeStrings(word1,word2))
print("Total --- %s seconds ---" % (time.time() - start_time))