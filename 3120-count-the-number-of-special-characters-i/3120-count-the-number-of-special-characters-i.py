class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        c=0
        s=set(list(word))
        vis=[]
        for i in s:
            if (i.lower() not in vis) and (i.upper() not in vis) and (i.lower() in word) and (i.upper() in word):
                vis.append(i)
                c+=1
        return c

# class Solution:
#     def numberOfSpecialChars(self, word: str) -> int:
#         s = set(word)
#         count = 0
        
#         for ch in s:
#             if ch.islower() and ch.upper() in s:
#                 count += 1
        
#         return count
