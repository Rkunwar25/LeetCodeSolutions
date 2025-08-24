class Solution(object):
    def minCost(self,cost,i,dp):
        if i>=len(cost):
            return 0
        if dp[i]!=-1:
            return dp[i]
        take1=cost[i]+self.minCost(cost,i+1,dp)
        take2=cost[i]+self.minCost(cost,i+2,dp)
        dp[i]=min(take1,take2)
        return dp[i]
    def minCostClimbingStairs(self, cost):
        dp=[-1]*len(cost)
        return min(self.minCost(cost,0,dp),self.minCost(cost,1,dp))