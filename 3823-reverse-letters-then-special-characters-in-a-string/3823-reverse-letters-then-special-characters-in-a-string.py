class Solution:
    def reverseByType(self, s: str) -> str:
        letters=[]
        special=[]
        for i in s:
            if i.isalpha():
                letters.append(i)
            if not i.isalnum():
                special.append(i)
        letters=letters[::-1]
        special=special[::-1]
        j=0
        k=0
        ans=""
        for i in s:
            if i.isalpha():
                ans+=letters[j]
                j+=1
            if not i.isalnum():
                ans+=special[k]
                k+=1
        return ans