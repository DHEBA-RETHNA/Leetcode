class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        """ans = []
        for i in nums:
            ans.append(i*i)
        return sorted(ans)"""  

        """for i in range(len(nums)):
            nums[i] = nums[i]*nums[i]
        nums.sort()
        return nums"""

        ans = [num ** 2 for num in nums]
        ans.sort()
        return ans  