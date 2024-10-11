class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        value = set(nums)
        ans = 0
        max = 0
        for i in value:
            if max < nums.count(i):
                max = nums.count(i)
                ans = i
        return ans