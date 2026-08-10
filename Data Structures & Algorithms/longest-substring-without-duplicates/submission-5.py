class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        
        longest = 0
        visited = []

        for start in s:
            if start in visited:
                index = visited.index(start)
                visited = visited[index + 1:]

            visited.append(start)
            longest = max(longest, len(visited))

        return longest