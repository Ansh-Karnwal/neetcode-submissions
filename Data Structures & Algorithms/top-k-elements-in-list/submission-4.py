class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = {}
        freq_array = [[] for i in range(len(nums) + 1)]
        for i in nums:
            freq_map[i] = 1 + freq_map.get(i, 0)
        for num, freq in freq_map.items():
            freq_array[freq].append(num)
        res = []
        for i in range(len(nums), 0, -1):
            for j in freq_array[i]:
                res.append(j)
                if len(res) == k:
                    return res
        

