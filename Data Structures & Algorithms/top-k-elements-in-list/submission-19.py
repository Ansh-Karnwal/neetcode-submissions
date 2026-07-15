class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_list = [[] for i in range(len(nums) + 1)]
        freq_map = {}
        for i in nums:
            freq_map[i] = freq_map.get(i, 0) + 1
        for i, j in freq_map.items():
            num_list[j].append(i)
        res = []
        for i in range(len(num_list)-1, -1,-1):
            for num in num_list[i]:
                res.append(num)
                if len(res) == k:
                    return res 