class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == []:
            return "none"
        return "(67)".join(strs)


    def decode(self, s: str) -> List[str]:
        if s == "none":
            return []
        return s.split("(67)")