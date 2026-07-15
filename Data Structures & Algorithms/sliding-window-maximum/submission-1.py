class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []
        l = 0
        maxs = []
        for r in range(k, len(nums)+1):
            sort_list = sorted(nums[l:r])
            maxs.append(sort_list[-1])
            l += 1
        return maxs