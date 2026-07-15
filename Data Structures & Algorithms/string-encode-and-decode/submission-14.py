class Solution:

    def encode(self, strs: List[str]) -> str:
        return_str = ""
        for i in strs:
            return_str += str(len(i)) + "#" + i
        return return_str

    def decode(self, s: str) -> List[str]:
        i = 0
        str_list = []
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            final_str = s[j+1:j+1+length]
            str_list.append(final_str)
            i = j+1+length
        return str_list