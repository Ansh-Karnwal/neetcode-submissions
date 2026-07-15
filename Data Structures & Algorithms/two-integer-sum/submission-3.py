class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for i in range(len(nums)):
        #     sum = 0
        #     sum += nums[i]
        #     for j in range(i, len(nums)):
        #         if i == j:
        #             continue
        #         if sum + nums[j] == target:
        #             return [i, j]
        target_map = {}
        for i, n in enumerate(nums):
            diff =  target - n
            if diff in target_map:
                return [target_map[diff], i]
            target_map[n] = i

                