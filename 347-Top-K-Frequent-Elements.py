class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnum = Counter(nums)
        return [x[0] for x in cnum.most_common(k)]
        