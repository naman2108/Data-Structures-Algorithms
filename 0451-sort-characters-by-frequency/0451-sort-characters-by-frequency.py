from collections import defaultdict
class Solution:
    def frequencySort(self, s: str) -> str:
        mp=defaultdict(int)
        for i in s:
            mp[i]+=1
        freqholder=[[] for _ in range(len(s)+1)]
        for i, j in mp.items():
            freqholder[j].append(i)
        ans=[]
        for i in range(len(freqholder)-1,-1,-1):
            for j in freqholder[i]:
                ans.extend([j]*i)
        return "".join(ans)            

        