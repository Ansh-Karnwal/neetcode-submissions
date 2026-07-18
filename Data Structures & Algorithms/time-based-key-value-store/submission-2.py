from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.time_map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_map[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        l, r = 0, len(self.time_map[key]) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if self.time_map[key][mid][-1] > timestamp:
                r = mid - 1
            elif self.time_map[key][mid][-1] < timestamp:
                l = mid + 1
            else:
                return self.time_map[key][mid][0]
        if r == -1:
            return ""
        return self.time_map[key][r][0]