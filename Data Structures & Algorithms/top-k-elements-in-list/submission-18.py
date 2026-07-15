class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = {}
        num_list = [[] for i in range(len(nums) + 1)]
        for i in nums:
            freq_map[i] = 1 + freq_map.get(i, 0)
        for num, freq in freq_map.items():
            num_list[freq].append(num)
        res = []
        for i in range(len(num_list) - 1, -1, -1):
            for num in num_list[i]:
                res.append(num)
                if len(res) == k:
                    return res
