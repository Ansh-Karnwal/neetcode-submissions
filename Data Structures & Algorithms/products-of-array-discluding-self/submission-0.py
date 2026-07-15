class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        for i in range(len(nums)):
            current = 1
            for p, j in enumerate(nums):
                if i == p:
                    continue
                current *= j
            res[i] = current
        return res
        
            

