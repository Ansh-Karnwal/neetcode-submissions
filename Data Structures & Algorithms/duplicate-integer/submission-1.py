class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        skip_index = 0
        for i in nums:
            for j in range(len(nums)):
                if j == skip_index:
                    continue
                if i == nums[j]:
                    return True
            skip_index += 1
        return False
        