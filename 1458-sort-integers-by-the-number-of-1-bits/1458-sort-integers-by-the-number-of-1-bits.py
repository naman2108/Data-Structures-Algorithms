class Solution:
    def count1(self,bini):
        cnt=0
        for i in bini:
            if i=='1':
                cnt+=1
        return cnt        

    def sortByBits(self, arr: List[int]) -> List[int]:
        return sorted(arr,key=lambda x:(bin(x).count('1'),x))
            




        