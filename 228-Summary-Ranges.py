class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ans = []
        i = 0
        while i < len(nums):
            start = nums[i]
            j = i
            while j < len(nums)-1 and nums[j]+1 == nums[j+1]:
                j += 1
            if j == i :
                ans.append(f\{nums[i]}\)
            else:
                ans.append(f\{start}->{nums[j]}\)
            i = j+1
        return ans