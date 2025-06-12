class Solution(object):
    def nextGreatestLetter(self, letters, target):
        if target not in letters:
            letters.append(target)
        letters=list(set(letters))
        letters.sort()
        if letters.index(target)==len(letters)-1:
            return letters[0]        
        return letters[letters.index(target)+1]