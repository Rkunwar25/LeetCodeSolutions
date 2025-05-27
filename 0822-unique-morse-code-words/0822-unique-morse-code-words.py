class Solution(object):
    def uniqueMorseRepresentations(self, words):
        mc=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        l=[]
        for i in words:
            w=""
            for j in i:
                w+=mc[ord(j)-ord('a')]
            l.append(w)
        return len(set(l))