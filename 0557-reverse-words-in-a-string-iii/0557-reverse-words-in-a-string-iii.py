class Solution:
    def reverseWords(self, s: str) -> str:
        ans=[]
        s=s.split(' ')
        for i in s:
            ans.append(i[::-1])
        return " ".join(ans)    

        

          
        