class Solution(object):
    def subarrayBitwiseORs(self, arr):
          res = set()
          prev = set()
    
          for num in arr:
            cur = {num}
            for x in prev:
                cur.add(num | x)
            res.update(cur)
            prev = cur
        
          return len(res)     