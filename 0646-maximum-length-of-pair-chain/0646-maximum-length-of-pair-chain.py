class Solution:
    def findLongestChain(self, pairs):
        # Step 1: sort by ending time
        pairs.sort(key=lambda x: x[1])
        
        count = 1
        prev_end = pairs[0][1]
        
        for i in range(1, len(pairs)):
            if pairs[i][0] > prev_end:
                count += 1
                prev_end = pairs[i][1]
                
        return count