class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        target_map = {}
        for i, n in enumerate(nums):
            difference = target - n
            if difference in target_map:
                return [target_map[difference], i]
            target_map[n] = i
        