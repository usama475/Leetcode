class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        Ans=[]
        right=len(numbers)-1
        left=0
        while left<right:
            if numbers[left]+numbers[right]>target:
                right-=1
            elif numbers[left]+numbers[right]<target:
                left+=1
            else:
                Ans.append(left+1)
                Ans.append(right+1)  
                return Ans  
                  