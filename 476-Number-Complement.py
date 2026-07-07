class Solution:
    def findComplement(self, num: int) -> int:
        n = (1 << num.bit_length()) - 1
        return n ^ num