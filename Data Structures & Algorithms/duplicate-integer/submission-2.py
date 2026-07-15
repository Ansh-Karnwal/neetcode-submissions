class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        the_set = set()
        for i in nums:
            if i in the_set:
                return True
            the_set.add(i)
        return False        