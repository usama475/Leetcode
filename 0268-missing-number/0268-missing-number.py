class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(0,n+1):
            if i not in nums:
                return i
        
        # n = len(nums)
        # total = n*(n+1)//2
        # for num in nums:
        #     total -= num
        # return total