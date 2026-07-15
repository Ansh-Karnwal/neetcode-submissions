class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        occ_map = {}
        k_arr = [[] for i in range(len(nums) + 1)]
        for i in nums:
            occ_map[i] = 1 + occ_map.get(i, 0)
        for val, freq in occ_map.items():
            k_arr[freq].append(val)
        res = []
        for i in range(len(nums), 0, -1):
            for j in k_arr[i]:
                res.append(j)
                if len(res) == k:
                    return res
        
