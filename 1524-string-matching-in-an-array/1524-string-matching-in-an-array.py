class Solution(object):
    def stringMatching(self, words):
        l=[]
        n=len(words)
        for i in range(n):
            for j in range(n):
                if i!=j and words[i] in words[j]:
                    l.append(words[i])
                    continue
        return list(set(l))