class Solution:
    def helper(self,i,j,m,n,dp):
        if i==m-1 and j==n-1:
            return 1
        if dp[i][j]!=-1:
            return dp[i][j]    
        ans=0
        if i+1<m:
            ans+=self.helper(i+1,j,m,n,dp) 
        if j+1<n:
            ans+=self.helper(i,j+1,m,n,dp)
        dp[i][j]=ans
        return dp[i][j]
    def uniquePaths(self, m: int, n: int) -> int:
        dp=[[-1]*(n) for _ in range(m)]
        return self.helper(0,0,m,n,dp)
                
        