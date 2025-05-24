class Solution(object):
    def rowAndMaximumOnes(self, mat):
        # d=dict()
        # for i in range(len(mat)):
        #     d[i]=mat[i].count(1)
        # mn=float('-inf')
        # for i,j in d.items():
        #     mn=max(mn,j)
        # l=[]
        # for i in d.keys():
        #     if d[i]==mn:
        #         l.append(i)
        # return [min(l),mn]
        max_count = -1
        row_index = -1
        for i, row in enumerate(mat):
            count_ones = row.count(1)
            if count_ones > max_count:
                max_count = count_ones
                row_index = i
        return [row_index, max_count]