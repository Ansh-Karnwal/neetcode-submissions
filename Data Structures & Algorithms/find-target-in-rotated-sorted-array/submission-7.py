class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            mid = l + (r - l) // 2
            if nums[mid] > nums[r]:
                l = mid + 1  # min is in right half
            else:
                r = mid      # min is at mid or left of mid

        min_idx = l  # no need for the -= 1 adjustment

        if target <= nums[-1]:
            l, r = min_idx, len(nums) - 1
        else:
            l, r = 0, min_idx - 1

        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                return mid

        return -1