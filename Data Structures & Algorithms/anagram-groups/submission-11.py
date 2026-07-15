class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs_map = defaultdict(list)
        for word in strs:
            characters = [0] * 26
            for c in word:
                characters[ord(c) - ord('a')] += 1
            strs_map[tuple(characters)].append(word)
        return list(strs_map.values())