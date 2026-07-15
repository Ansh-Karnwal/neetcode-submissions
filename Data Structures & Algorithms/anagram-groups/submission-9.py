class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        str_map = defaultdict(list)
        for s in strs:
            chr_list = [0] * 26
            for c in s:
                chr_list[ord(c) - ord('a')] += 1
            str_map[tuple(chr_list)].append(s)
        return list(str_map.values())
