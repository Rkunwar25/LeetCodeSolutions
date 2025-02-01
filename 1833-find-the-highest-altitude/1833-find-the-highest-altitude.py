class Solution(object):
    def largestAltitude(self, gain):
        l=[0]
        for i in range(1,len(gain)):
            l.append(l[i-1]+gain[i-1])
        l.append(l[len(l)-1]+gain[len(gain)-1])
        print(l)
        return max(l)