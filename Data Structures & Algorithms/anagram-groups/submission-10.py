class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        str_map = defaultdict(list)
        for word in strs:
            char_list = [0] * 26
            for c in word:
                char_list[ord(c) - ord('a')] += 1
            str_map[tuple(char_list)].append(word)
        return list(str_map.values())