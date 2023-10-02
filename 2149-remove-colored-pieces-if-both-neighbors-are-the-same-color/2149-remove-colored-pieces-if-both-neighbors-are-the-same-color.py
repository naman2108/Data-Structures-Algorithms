class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        alice=0
        bob=0
        for i in range(1,len(colors)-1):
            if  colors[i]=='A' and colors[i-1]==colors[i] and colors[i]==colors[i+1]:
                alice+=1
            if colors[i]=='B' and colors[i-1]==colors[i] and colors[i]==colors[i+1]:
                bob+=1
        return True if alice>bob else False         

        