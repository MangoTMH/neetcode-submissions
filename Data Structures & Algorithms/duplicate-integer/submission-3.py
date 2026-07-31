class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums) == 0:
            return False

        seen = []
        for i in range(len(nums)):
            if nums[i] in seen:
                return True
            seen.append(nums[i])
        return False
