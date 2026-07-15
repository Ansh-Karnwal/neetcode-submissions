class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = {}
        nums_arr = [[] for i in range(len(nums) + 1)]
        for i in nums:
            freq_map[i] = 1 + freq_map.get(i, 0)
        for num, v in freq_map.items():
            nums_arr[v].append(num)
        res = []
        for i in range(len(nums_arr)-1, 0, -1):
            for j in nums_arr[i]:
                res.append(j)
                if len(res) == k:
                    return res
