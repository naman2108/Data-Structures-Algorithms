class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        ans=[]
        for i in bank:
            x=i.count('1')
            if x>0:
                ans.append(x)
        if len(ans)<2:
            return 0
        s=0
        for i in range(len(ans)-1):
            s+=ans[i]*ans[i+1]
        return s                
        
        