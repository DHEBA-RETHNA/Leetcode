class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums.sort()
        nums1 = []
        for i in nums:
            if i in nums1:
                continue
            nums1.append(i)
        if len(nums1) < 3:
            return nums1[-1]
        else:
            return nums1[-3]