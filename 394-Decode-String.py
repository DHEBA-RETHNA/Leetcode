class Solution:
    def decodeString(self, s: str) -> str:
        numstack = []
        strstack = []
        currnum = 0
        currstr = ""

        for ch in s:
            if ch.isdigit():
                currnum = currnum * 10 + int(ch)

            elif ch == "[":
                numstack.append(currnum)
                strstack.append(currstr)
                currnum = 0
                currstr = ""

            elif ch == "]":
                repeat = numstack.pop()
                prev = strstack.pop()
                currstr = prev + currstr * repeat

            else:
                currstr += ch

        return currstr