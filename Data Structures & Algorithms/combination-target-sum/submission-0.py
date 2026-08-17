class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        combinations = []
        
        def dfs(i, total):
            if total == target:
                res.append(combinations.copy())
                return
            if total > target or i >= len(nums):
                return

            # add itself
            combinations.append(nums[i])
            dfs(i, total + nums[i])
            combinations.pop()

            # add next 
            dfs(i+1, total)

            i += 1
        
        dfs(0, 0)
        return res if res else []