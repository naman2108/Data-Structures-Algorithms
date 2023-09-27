class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        finalstr = 0
        if k==1:
            return s[0]
        
        # Calculate the length of the decoded string
        for i in s:
            if i.isalpha():
                finalstr += 1
            if i.isdigit():
                finalstr *= int(i)
        
        for i in range(len(s) - 1, -1, -1):
            char = s[i]
            if char.isdigit():
                digit = int(char)
                finalstr //= digit
                k %= finalstr  # Update k after modifying finalstr
                
            elif char.isalpha():
                if k == finalstr or k==0:
                    return char
                finalstr -= 1
        
        return ""


                
                        

            



        