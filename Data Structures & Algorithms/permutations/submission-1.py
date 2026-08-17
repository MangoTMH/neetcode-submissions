class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        used = [False] * len(nums)

        def dfs(i):
            if len(subset) >= len(nums):
                res.append(subset.copy())
                return
            
            for i in range(len(nums)):
                if used[i]:
                    continue
                used[i] = True
                subset.append(nums[i])
                dfs(i)
                subset.pop()
                used[i] = False
        
        dfs(0)
        return res