class Solution(object):
    def nextGreaterElements(self, nums):
        l = []
        n = len(nums)
        for idx, i in enumerate(nums):
            # Rotate starting from current index to simulate circular behavior
            nm = nums[idx+1:] + nums[:idx]
            found = False
            for j in nm:
                if j > i:
                    l.append(j)
                    found = True
                    break
            if not found:
                l.append(-1)
        return l
