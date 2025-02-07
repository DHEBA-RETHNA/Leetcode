class Solution:
    def intToRoman(self, num: int) -> str:
        hmap = { 1:'I', 4:'IV', 5:'V', 9:'IX', 10:'X', 40:'XL', 50:'L', 90:'XC', 100:'C',
        400:'CD', 500:'D', 900:'CM', 1000:'M' }
        ans = \\
        i = 0
        while (num > 0):
            x = num % 10
            num //= 10
            ran = \\
            if x == 4 or x == 9:
                ran = hmap[x * (10 ** i)]
            elif x >= 5:
                ran = ran + hmap[5 * (10 ** i)]
                x -= 5
                ran = ran + hmap[1 * (10 ** i)] * x
            else:
                ran = ran + hmap[1 * (10 ** i)] * x
            ans = ran + ans
            i += 1
        return ans