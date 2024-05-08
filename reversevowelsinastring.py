class Solution:
    def reverseVowels(self, s: str) -> str:
        listedstr = list(s)
        boolvow = [False] * len(listedstr)
        vowstr = ''
        index = 0
        for i in s:
            if i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U':
                vowstr += i
                boolvow[index] = True
            index +=1
        if vowstr == '':
            return s
        vowindex = len(vowstr)-1
        index = 0
        for i in s:
            if boolvow[index] == True:
                listedstr[index] = vowstr[vowindex]
                vowindex -= 1
                if vowindex<= -1:
                    break
            index += 1
        return "".join(listedstr)

# class Solution:
#     def reverseVowels(self, s: str) -> str:
#         s = list(s) # convert string to list
#         vowels = set("aeiouAEIOU")
#         low = 0
#         high = len(s) - 1
#         while low < high:
#             if s[low] not in vowels:
#                 low += 1
#             elif s[high] not in vowels:
#                 high -= 1
#             else:
#                 s[low], s[high] = s[high], s[low] # swap the chars
#                 low += 1
#                 high -= 1
#         return "".join(s) # convert list to string


myobj = Solution()
sample = 'Live on evasions? No, I save no evil.'
print(myobj.reverseVowels(sample))
