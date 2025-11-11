class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # non_over= []
        # for i in range(len(intervals)): 
        #     for j in len(intervals[i]):
        #         if intervals[j] in intervals[j]+1:
        intervals.sort(key=lambda x: x[0])
        
        merged = []
        
        # Step 2: Iterate and merge
        for interval in intervals:
            # If merged list is empty OR no overlap → simply add the interval
            if not merged or interval[0] > merged[-1][1]:
                merged.append(interval)
            else:
                # Overlap → merge with the last interval
                merged[-1][1] = max(merged[-1][1], interval[1])
        
        return merged