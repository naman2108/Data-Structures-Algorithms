from collections import defaultdict
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        mp=defaultdict(int)
        for i in t:
            mp[i]+=1
        for i in s:
            mp[i]-=1
        for i,j in mp.items():
            if j>0:
                return i        



        
        