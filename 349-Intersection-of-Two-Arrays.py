class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1 = set(nums1)
        nums2 = set(nums2)
        ans = []
        for i in nums1:
            if i in nums2:
                ans.append(i)
        return ans