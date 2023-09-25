class Solution:
    def helper(self,i,j,n,m,obstacleGrid,dp):
        if i==n-1 and j==m-1:
            return 1
        if dp[i][j]!=-1:
            return dp[i][j]    
        ans=0
        if i+1<n and obstacleGrid[i][j]!=1:
            ans+=self.helper(i+1,j,n,m,obstacleGrid,dp)
        if j+1<m and obstacleGrid[i][j]!=1:
            ans+=self.helper(i,j+1,n,m,obstacleGrid,dp)
        dp[i][j]=ans
        return dp[i][j]       
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n=len(obstacleGrid)
        m=len(obstacleGrid[0])
        dp=[[-1] * (m) for _ in range(n)]
        if obstacleGrid[0][0]==1 or obstacleGrid[n-1][m-1]==1:
            return 0
        return self.helper(0,0,n,m,obstacleGrid,dp)
    


        