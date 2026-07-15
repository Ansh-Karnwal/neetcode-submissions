class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        word_map = defaultdict(list)
        for i in strs:
            chrs = [0] * 26
            for j in i:
                chrs[ord(j) - ord('a')] += 1
            word_map[tuple(chrs)].append(i)
        return list(word_map.values())