from collections import defaultdict
class Solution:
    def frequencySort(self, s: str) -> str:
        mp=defaultdict(int)
        for i in s:
            mp[i]+=1
        bucket=[[]  for _ in range(len(s)+1)]
        for i,j in mp.items():
            bucket[j].append(i)
        res=[]
        for i in range(len(bucket)-1,0,-1):
            for char in bucket[i]:
                res.extend([char]*i)
        return "".join(res)        

        