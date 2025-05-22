class Solution(object):
    def arrangeWords(self, text):
        words=text.split(' ')
        words[0]=words[0].lower()
        words.sort(key=len)
        words[0]=words[0].capitalize()
        return ' '.join(words)