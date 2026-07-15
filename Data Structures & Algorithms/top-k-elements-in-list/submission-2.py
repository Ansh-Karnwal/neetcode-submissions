class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = {}
        for i in nums: 
            freq_map[i] = 1 + freq_map.get(i, 0)
        mapper = [[] for i in range(len(nums) + 1)]
        for n, f in freq_map.items():
            mapper[f].append(n)
        res = []
        for i in range(len(mapper)-1, 0, -1):
            for n in mapper[i]:
                res.append(n)
                if len(res) == k:
                    return res
            