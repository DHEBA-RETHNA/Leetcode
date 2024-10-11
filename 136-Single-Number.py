class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        value = set(nums)
        for i in value:
            c = nums.count(i)
            if c == 1:
                return i