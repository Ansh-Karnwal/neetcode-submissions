class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        num_set = set(nums)
        for i in num_set:
            if (i - 1) not in num_set:
                length = 1
                while i + length in num_set:
                    length += 1
                longest = max(length, longest)
        return longest