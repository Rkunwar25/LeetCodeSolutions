class Solution(object):
    def kthSmallest(self, matrix, k):
       l=list()
       for i in range(len(matrix)):
           for j in range(len(matrix[i])):
              l.append(matrix[i][j])
       l.sort()
       return l[k-1]