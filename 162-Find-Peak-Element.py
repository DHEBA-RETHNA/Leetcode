class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        maxx = max(nums)
        return nums.index(maxx)