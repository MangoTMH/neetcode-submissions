class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)

        for i in nums:
            freq[i] += 1
    
        sort = sorted(freq.items(), key=lambda item: item[1], reverse=True)

        answer = []
        for j in range(k):
            answer.append(sort[j][0])
        
        return answer