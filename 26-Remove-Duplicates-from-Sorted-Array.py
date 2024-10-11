class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index = 0
        while index < len(nums):
            if nums[index] in nums[:index]:
                nums.remove(nums[index])
            else:
                index += 1
        return len(nums)
