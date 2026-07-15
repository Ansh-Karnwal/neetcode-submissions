class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        target_map = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in target_map:
                return [target_map[diff], i]
            target_map[n] = i
                