# class Solution:
#     def minDeletionSize(self, strs: List[str]) -> int:
#         ls=[]
#         for i in strs:
#             ls.append(list(i))
#         ls=list(map(list,zip(*ls)))
#         c=0
#         for i in range(len(ls)):
#             if ls[i]!=sorted(ls[i]):
#                 c+=1
#         return c
class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        rows, cols = len(strs), len(strs[0])
        deletions = 0

        for c in range(cols):
            for r in range(1, rows):
                if strs[r][c] < strs[r-1][c]:
                    deletions += 1
                    break

        return deletions
