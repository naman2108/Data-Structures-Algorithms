from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        mp=defaultdict(int)
        ans=[]
        for i in nums:
            mp[i]+=1
        for i,j in mp.items():
            if j>len(nums)//3:
                ans.append(i)
        return ans         

        