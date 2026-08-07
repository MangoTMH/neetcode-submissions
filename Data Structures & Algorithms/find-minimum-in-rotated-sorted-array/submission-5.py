class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        res = 0
        first = nums[0]
        last = nums[-1]

        if first < last:
            return first
        else:
            highest = first
            while l <= r:
                mid = (l + r) // 2
                res = nums[mid]
                if res < nums[mid - 1]:
                    return res
                else:
                    if highest > res:
                        r = mid - 1
                    else:
                        highest = res
                        l = mid + 1
        
        return res