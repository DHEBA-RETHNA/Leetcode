class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        \\\
        Do not return anything, modify nums in-place instead.
        \\\
        if nums == 0 or nums == 1:
            return nums
        else:
            for i in range(len(nums)):
                key = nums[i]
                j = i-1
                while j >= 0 and nums[j]==0:
                    nums[j+1] = nums[j]
                    j -= 1
                nums[j+1] = key
        return nums 