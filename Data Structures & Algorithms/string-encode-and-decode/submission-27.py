class Solution:

    def encode(self, strs: List[str]) -> str:
        final_str = ""
        for i in strs:
            final_str += str(len(i)) + "#" + i
        return final_str

    def decode(self, s: str) -> List[str]:
        res_list = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            decode_str = s[j+1:j+1+length]
            res_list.append(decode_str)
            i = j+1+length
        return res_list