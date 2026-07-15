class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = {}
        mapper_arr = [[] for i in range(len(nums) + 1)]
        for i in nums:
            freq_map[i] = 1 + freq_map.get(i, 0)
        for v, f in freq_map.items():
            mapper_arr[f].append(v)
        res = []
        for i in range(len(mapper_arr) - 1, 0, -1):
            for j in mapper_arr[i]:
                res.append(j)
                if len(res) == k:
                    return res
