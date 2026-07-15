class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for string in strs:
            char_list = [0] * 26
            for c in string:
                char_list[ord(c) - ord('a')] += 1
            res[tuple(char_list)].append(string)
        return list(res.values())