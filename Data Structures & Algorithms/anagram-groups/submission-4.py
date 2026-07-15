class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        num_map = defaultdict(list)
        for i in strs:
            chars = [0] * 26
            for c in i:
                chars[ord(c) - ord('a')] += 1
            num_map[tuple(chars)].append(i)
        return list(num_map.values())
