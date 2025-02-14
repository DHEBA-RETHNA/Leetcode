class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        \\\if len(set(nums)) >= 3:
            for i in range(len(nums) - 2):
                for j in range(i+1, len(nums) - 1):
                    for k in range(j+1, len(nums)):
                        if nums[i] < nums[k] < nums[j]:
                            return True
             return False
        return False\\\
        stack = []
        minval = nums[0]
        for i in nums[1:]:
            while stack and i >= stack[-1][0]:
                stack.pop()
            if stack and i > stack[-1][1]:
                return True
            stack.append([i,minval])
            minval = min(minval, i)
        return False