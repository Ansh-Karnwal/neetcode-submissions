class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        str_map = {}
        for s in strs:
            current_str = ''.join(sorted(s))
            str_map[current_str] = str_map.get(current_str, [])
            str_map[current_str].append(s)
        print(str_map)
        final_list = []
        for k in str_map:
            final_list.append(str_map[k])
        return final_list