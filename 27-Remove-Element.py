class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        index = 0
        c = len(nums)
        while index <= c:
            if val in nums[:index+1]:
                nums.remove(val)
                print(c)
            index += 1
        return len(nums)