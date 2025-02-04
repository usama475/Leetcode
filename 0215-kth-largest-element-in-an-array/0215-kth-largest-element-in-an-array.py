class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # for i in range(len(nums)):
        
        for i in range(k): 
         max_num = max(nums)  
         nums.remove(max_num)  
        return max_num  