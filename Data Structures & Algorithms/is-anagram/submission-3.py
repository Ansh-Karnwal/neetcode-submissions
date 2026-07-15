class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        # s_set = set()
        # t_set = set()
        # for i in range(len(s)):
        #     s_set.add(s[i])
        # for i in range(len(t)):
        #     t_set.add(t[i])
        # if len(t_set - s_set) > 0 or len(s_set - t_set) > 0:
        #     return False
        # return True
        s_dict = {}
        t_dict = {}
        for i in range(len(s)):
            if s[i] in s_dict.keys():
                s_dict[s[i]] += 1
                continue
            s_dict[s[i]] = 1
        for i in range(len(t)):
            if t[i] in t_dict.keys():
                t_dict[t[i]] += 1
                continue
            t_dict[t[i]] = 1  
        for i, j in s_dict.items():
            try:
                if j != t_dict[i]:
                    return False
            except KeyError:
                return False
        return True

            
        