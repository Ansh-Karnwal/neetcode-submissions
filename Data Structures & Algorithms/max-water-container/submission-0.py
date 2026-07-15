class Solution:
    def maxArea(self, heights: List[int]) -> int:
        current_product = float('-inf')
        #current_product = max(current_product, (r-l) * min(heights[l], heights[r]))

        l, r = 0, len(heights) - 1
        while l < r:
            current_product = max(current_product, (r-l) * min(heights[l], heights[r]))
            if heights[l] < heights[r]:
                l += 1
            elif heights[r] < heights[l]:
                r -= 1
            else:
                l += 1
        
        return current_product
            
            

