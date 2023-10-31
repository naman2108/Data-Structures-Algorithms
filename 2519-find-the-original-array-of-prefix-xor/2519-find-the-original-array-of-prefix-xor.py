class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        if len(pref)==1:
            return pref
        ans=[]
        ans.append(pref[0])
        i=1
        j=0
        while i<len(pref):
            ans.append(pref[i]^pref[j])
            i+=1
            j+=1
        return ans    


        