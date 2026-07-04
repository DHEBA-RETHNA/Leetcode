class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [1]
        suf = [1]
        ans = []
        for i in range(len(nums)):
            prepro = pre[-1] * nums[i]
            pre.append(prepro)
        for j in range(len(nums)-1, -1, -1):
            sufpro = suf[-1] * nums[j]
            suf.append(sufpro)
        for k in range(len(nums)):
            product = pre[k] * suf[len(suf) - 2 - k]
            ans.append(product)
        return ans