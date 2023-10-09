class Solution:
    def firstoc(self,nums,target):
        l=0
        r=len(nums)-1
        first=-1
        while l<=r:
            mid=(l+r)//2
            if nums[mid]==target:
                first=mid
                r=mid-1

            elif nums[mid]<target:
                l=mid+1
            else:
                r=mid-1  
        return first                
    def lastoc(self,nums,target):
        l=0
        r=len(nums)-1
        last=-1
        while l<=r:
            mid=(l+r)//2
            if nums[mid]==target:
                last=mid
                l=mid+1
            elif nums[mid]<target:
                l=mid+1
            else:
                r=mid-1

        return last

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first=self.firstoc(nums,target)
        second=self.lastoc(nums,target)
        if first==-1:
            return [-1,-1]
        else:
            return [first,second]    

        