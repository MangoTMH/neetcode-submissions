class Solution:
    def findMin(self, nums: List[int]) -> int:
        sort = sorted(nums)
        lowest = sort[0]

        return lowest