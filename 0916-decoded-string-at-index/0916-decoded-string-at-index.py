class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        finalstr=0
        for i in s:
            if i.isalpha():
                finalstr+=1
            elif i.isdigit():
                finalstr*=int(i)
        for i in range(len(s)-1,-1,-1):
            if s[i].isalpha():
                if finalstr==k or k==0:
                    return s[i]
                finalstr-=1
            elif s[i].isdigit():
                finalstr=finalstr//int(s[i])
                k%=finalstr        

        return ""