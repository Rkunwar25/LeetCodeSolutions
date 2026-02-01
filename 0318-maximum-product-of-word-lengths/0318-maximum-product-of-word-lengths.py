class Solution:
    def maxProduct(self, words: List[str]) -> int:
        words=sorted(words,key=len)
        words=words[::-1]
        mx=0
        for i in range(len(words)):
            for j in range(i+1,len(words)):
                if set(words[i]).isdisjoint(set(words[j])):
                    mx=max(mx,len(words[i])*len(words[j]))
                    break
        return mx