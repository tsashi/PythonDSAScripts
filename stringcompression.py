class Solution:
    def compress(self, chars: list[str]) -> int:
        n = len(chars)
        prev = chars[0]
        curr = chars[0]
        prevposition = 0
        count = 1
        #lencount = len(str(count))
        #strcount = str(count)
        for i in range(1,n):
            curr = chars[i]
            if prev==curr:
                count+=1
            else:
                if count==1:
                    chars[prevposition]=prev
                    prev = curr
                    prevposition += 1
                elif count>1:
                    chars[prevposition]=prev
                    lencount = len(str(count))
                    strcount = str(count)
                    prevposition += 1
                    for j in range(lencount):
                        chars[prevposition+j]=strcount[j]
                    prev = curr
                    prevposition += lencount
                    count = 1
        if count==1:
            chars[prevposition]=prev
            prev = curr
            prevposition += 1
        elif count>1:
            chars[prevposition]=prev
            lencount = len(str(count))
            strcount = str(count)
            prevposition += 1
            for j in range(lencount):
                chars[prevposition+j]=strcount[j]
            prev = curr
            prevposition += lencount
            count = 1
        return prevposition
    
myobj = Solution()
chars = ["a","a","b","b","c","c","c"]
retlen = myobj.compress(chars)
print(retlen)
print(chars[:retlen])