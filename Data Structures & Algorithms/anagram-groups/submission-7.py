class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        chr_map = defaultdict(list)
        for i in strs:
            chrs = [0] * 26
            for c in i:
                chrs[ord(c) - ord('a')] += 1
            chr_map[tuple(chrs)].append(i)
        return list(chr_map.values())