class Solution:
    def maxArea(self, heights: List[int]) -> int:
        current_product = 0

        l, r = 0, len(heights) - 1
        while l < r:
            current_product = max(current_product, (r-l) * min(heights[l], heights[r]))
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        
        return current_product
            
            

