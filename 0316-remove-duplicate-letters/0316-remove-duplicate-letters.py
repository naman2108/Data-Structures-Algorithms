class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        d={char:index for index,char in enumerate(s)}
        res=[]
        for index,char in enumerate(s):
            if char not in res:
                while res and index < d[res[-1]] and char<res[-1]:
                    res.pop()
                res.append(char)
                    
        return "".join(res)     