class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        
        cnt=0
        i=0
        j=0
        arr=[]
        while j<len(dist) and i<len(speed):
            arr.append(dist[j]/speed[i])
            i+=1
            j+=1
        arr.sort()    
        for i in range(len(arr)):
            if arr[i]<=i:
                break
            cnt+=1
        return cnt             
