class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map =  {}
        lister = [[] for i in range(len(nums) + 1)]
        for i in nums:
            freq_map[i] = 1 + freq_map.get(i, 0)
        for num, freq in freq_map.items():
            lister[freq].append(num)
        res = []
        for i in range(len(lister) - 1, -1, -1):
            for i in lister[i]:
                res.append(i)
                if len(res) == k:
                    return res