class Solution(object):
    def numDifferentIntegers(self, word):
        # l=re.split(r"[a-z]",word)
        # st=list(set(l))
        # nl=[]
        # for i in st:
        #     if (i!='') and (int(i) not in nl):
        #         nl.append(int(i))
        # return len(nl)
        numbers = set(map(int, re.findall(r"\d+", word)))
        return len(numbers)