class Solution(object):
    def constructRectangle(self, area):
        n = int(math.sqrt(area))
        for i in range(n, 0, -1):
            if area % i == 0:
                return [area // i, i]