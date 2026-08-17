class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def dfs(i):
            if len(subset) >= len(nums):
                res.append(subset.copy())
                return
            
            for i in range(len(nums)):
                print(subset)
                if nums[i] in subset:
                    continue
                subset.append(nums[i])
                dfs(i)
                subset.pop()
        
        dfs(0)
        return res