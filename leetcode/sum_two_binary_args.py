# https://leetcode.com/problems/add-binary/
#
# Given two binary strings a and b, return their
# sum as a binary string.
# Example
# Input: a = "11", b = "1"
# Output: "100"
# Example
# Input: a = "1010", b = "1011"
# Output: "10101"


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        max_len = max(len(a), len(b))
        a = a.zfill(max_len)
        b = b.zfill(max_len)

        carry = 0
        result = ''

        for i in range(max_len - 1, -1, -1):
            res = int(a[i]) + int(b[i]) + carry
            if res == 1:
                res = 1
                carry = 0

            elif res == 2:
                res = 0
                carry = 1
            elif res == 3:
                res = 1
                carry = res % 2
            else:
                res = 0
                carry = 0
            result += str(res)
        if carry != 0: result = '1' + result[::-1]
        return result[::-1]


print(Solution.addBinary(Solution, '110', '101'))
