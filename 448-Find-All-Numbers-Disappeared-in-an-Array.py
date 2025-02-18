class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        \\\for i in range(1,len(nums)+1):
            if i in nums:
                nums = list(filter(lambda x : x != i, nums))
            else:
                nums.append(i)
        return nums\\\                         #time complexity: O(n^2)
        \\\ans = set()
        for i in range(1,len(nums)+1):
            if i not in nums:
                ans.add(i)
        return list(ans)\\\                    #time complexity: O(n^2)
        ans = set(range(1, len(nums)+1))
        for i in nums:
            if i in ans:
                ans.remove(i)
        return list(ans)                      #time complexity: O(n)
