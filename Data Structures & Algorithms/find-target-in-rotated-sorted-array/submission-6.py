class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums) - 1
        cur = 0

        while l <= r:
            mid = (l+r) // 2
            cur = nums[mid] 
            if cur == target:
                return mid
            if nums[l] <= nums[mid]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if cur < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1

        return -1