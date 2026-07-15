class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_list = [[] for i in range(len(nums) + 1)]
        num_map = {}
        for i in nums:
            num_map[i] = num_map.get(i, 0) + 1
        for num, freq in num_map.items():
            num_list[freq].append(num)
        res = []
        for i in range(len(num_list)-1,-1,-1):
            for num in num_list[i]:
                res.append(num)
                if len(res) == k:
                    return res


