class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = []
        for i in range(len(temperatures) - 1):
            days = 0
            for j in range(i + 1, len(temperatures)):
                days += 1
                if temperatures[j] > temperatures[i]:
                    res.append(days)
                    break
                if j == len(temperatures) - 1:
                    res.append(0)
        if res:
            res.append(0)
        return res