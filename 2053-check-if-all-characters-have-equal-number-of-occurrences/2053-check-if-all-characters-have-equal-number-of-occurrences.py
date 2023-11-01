from collections import defaultdict

class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        cnt = 0
        mp = defaultdict(int)
        for i in s:
            mp[i] += 1
        first_count = None
        for i in mp:
            if first_count is None:
                first_count = mp[i]
            elif mp[i] != first_count:
                return False
        return True
                
        
