class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        char_count = {}
        maxf = 0
        res = 0
        for r in range(len(s)):
            char_count[s[r]] = char_count.get(s[r], 0) + 1
            maxf = max(maxf, char_count[s[r]])
            while (r - l + 1) - maxf > k:
                char_count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res            