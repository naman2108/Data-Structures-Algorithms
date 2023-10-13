class Solution:
    def minclimb(self,cost,n,dp):
        if n<=1:
            return 0
        if n==2:
            dp[n]=min(cost[0],cost[1])
        if dp[n]!=-1:
            return dp[n]    
        dp[n]=min(self.minclimb(cost,n-1,dp)+cost[n-1],self.minclimb(cost,n-2,dp)+cost[n-2])
        return dp[n]
                
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n=len(cost)
        dp=[-1]*(n+1)
        return self.minclimb(cost,n,dp)
        
        
        

        