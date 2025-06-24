class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = []
        for cd in candies:
            if cd + extraCandies >= max(candies):
                result.append(True)
            else:
                result.append(False)
        return result