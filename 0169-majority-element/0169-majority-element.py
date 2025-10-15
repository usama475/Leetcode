class Solution:
    def majorityElement(self, nums: List[int]) -> int:
      N = len(nums) 
      for num in nums:
        if nums.count(num) > N//2: 
            return num
       