class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_group = defaultdict(list)

        for i in strs:
            sort = ''.join(sorted(i))
            anagram_group[sort].append(i)
        
        return list(anagram_group.values())