class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        \\\ans = []
        for i in range(len(nums) - 2):
            for j in range(i + 1, len(nums) - 1):
                for k in range(j + 1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0 and sorted([nums[i], nums[j], nums[k]]) not in ans:
                        ans.append(sorted([nums[i], nums[j], nums[k]]))
        return ans\\\

        ans = []
        nums.sort()
        for indx, val in enumerate(nums):
            if (indx>0) & (val == nums[indx-1]):
                continue
            left = (indx + 1)
            right = (len(nums) - 1)
            while left < right:
                currentSum = val + nums[left] + nums[right]
                if currentSum > 0:
                    right -= 1
                elif currentSum < 0:
                    left += 1
                else:
                    ans.append([val, nums[left], nums[right]])
                    left += 1
                    while (left < right) & (nums[left] == nums[left-1]):
                        left += 1 
        return ans