class Solution(object):
    def oddCells(self, m, n, indices):
        l=[[0]*n for _ in range(m)]
        count=0
        for i in indices:
            r=i[0]
            c=i[1]
            print(r,c)
            for j in range(n):
                l[r][j]+=1
                
            for j in range(m):
                l[j][c]+=1
                
        for i in l:
            for j in range(len(i)):
                if i[j]%2!=0:
                    count+=1
        return count
        