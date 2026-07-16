class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)
        
        fleets = 0
        cur_p = cur_s = -1
        for p, s in cars:
            if cur_p == -1 or (target - p) * cur_s > (target - cur_p) * s:
                fleets += 1
                cur_p, cur_s = p, s
        return fleets