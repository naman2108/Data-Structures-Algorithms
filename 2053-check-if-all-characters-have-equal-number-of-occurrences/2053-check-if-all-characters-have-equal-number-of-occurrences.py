from collections import defaultdict

class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        cnt = 0
        mp = defaultdict(int)
        for i in s:
            mp[i] += 1
        for i,j in mp.items():
            if j!=mp[s[0]]:
                return False
        return True        

        
