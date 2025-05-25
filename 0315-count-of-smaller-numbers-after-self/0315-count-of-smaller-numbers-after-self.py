class Solution(object):
    def countSmaller(self, nums):
        res = []
        sorted_list = []

        for num in reversed(nums):
            index = bisect.bisect_left(sorted_list, num)
            res.append(index)
            bisect.insort(sorted_list, num)

        return res[::-1]