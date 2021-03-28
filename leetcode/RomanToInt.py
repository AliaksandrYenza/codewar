# https://leetcode.com/problems/roman-to-integer/
# Input: s = "MCMXCIV"
# Output: 1994
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
import roman as roman


class Solution:


    def romanToInt(self, s: str) -> int:
        rule_add = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        rule_div = {
            ('I', 'V'): 3,
            ('I', 'X'): 8,
            ('X', 'L'): 30,
            ('X', 'C'): 80,
            ('C', 'D'): 300,
            ('C', 'M'): 800
        }
        number = 0
        prev_l = None
        for l in s:
            if prev_l and rule_add[l] > rule_add[prev_l]:
                number += rule_div[(prev_l, l)]
                print(number)
            else:
                number += rule_add[l]
                print(number)
            prev_l = l
        return number


    if __name__ == '__main__':
        s = 'MCMXCIV'
        f = romanToInt('self', s)

