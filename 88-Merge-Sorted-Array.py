class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        \\\
        Do not return anything, modify nums1 in-place instead.
        \\\
        for i in range(1,n+1):
            nums1.pop()
        nums1 += nums2
        for i in range(m+n):
            for j in range(i+1,m+n):
                if nums1[i] >= nums1[j]:
                    nums1[i],nums1[j] = nums1[j],nums1[i]