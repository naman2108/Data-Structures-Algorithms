class Solution:
    def candy(self, ratings: List[int]) -> int:
        n=len(ratings)
        candy=[1]*n
        for i in range(1,n):
            if ratings[i]>ratings[i-1]:
                candy[i]=candy[i-1]+1
            else:
                candy[i]=1
        for i in reversed(range(n-1)):
            if ratings[i]>ratings[i+1]:
                candy[i]=max(candy[i],candy[i+1]+1)
        return sum(candy)                    
        