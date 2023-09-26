class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs)==0:
            return ""
        strs.sort()
        first=strs[0]
        last=strs[-1]
        i=0
        ans=''
        while i<len(first) and first[i]==last[i]:
            ans+=first[i]
            i+=1
        return ans        
        
        