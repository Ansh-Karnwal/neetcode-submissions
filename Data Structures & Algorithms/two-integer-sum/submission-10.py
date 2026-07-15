class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        val_map = {} # value : index
        for i, n in enumerate(nums):
            diff = target - n
            if diff in val_map:
                return [val_map[diff], i]
            val_map[n] = i