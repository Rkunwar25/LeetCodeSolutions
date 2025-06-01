class Solution(object):
    def sortPeople(self, names, heights):
       for i in range(len(names)):
          for j in range(0,len(names)-1-i):
             if heights[j]<heights[j+1]:
                 heights[j],heights[j+1]=heights[j+1],heights[j]
                 names[j],names[j+1]=names[j+1],names[j]
       return names