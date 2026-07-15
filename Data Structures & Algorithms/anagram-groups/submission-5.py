class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        str_map = defaultdict(list)
        for i in strs:
            chrs = [0] * 26
            for c in i:
                chrs[ord(c) - ord('a')] += 1
            str_map[tuple(chrs)].append(i)
        return list(str_map.values())