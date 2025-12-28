class Solution:
    def similarPairs(self, words: List[str]) -> int:
        count=0
        # l=[]
        n=len(words)
        for i in range(n):
            for j in range(i+1,n):
                if sorted(list(set(words[i])))==sorted(list(set(words[j]))):
                    count+=1
        return count