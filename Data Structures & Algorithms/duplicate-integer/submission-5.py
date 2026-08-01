class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()

        if len(nums) == 0:
            return False

        for i in range(len(nums)):
            if nums[i] in seen:
                return True
            seen.add(nums[i])
        return False    