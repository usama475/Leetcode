class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()   #-4,-1,-1,0,1,2
        Set=set()
        Ans=[]
        for i in range(len(nums)-2):
            j=i+1
            k=len(nums)-1
            while j<k:
                total=nums[i]+nums[j]+nums[k]
                if total==0:
                    Set.add((nums[i],nums[j],nums[k]))
                    k-=1
                elif total>0:
                    k-=1
                else:
                    j+=1
        return list(Set)
           