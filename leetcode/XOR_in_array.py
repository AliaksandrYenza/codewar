# 1486. XOR Operation in an Array
# https://leetcode.com/problems/xor-operation-in-an-array/
#
# Given an integer n and an integer start.
# Define an array nums where nums[i] = start + 2*i (0-indexed) and n == nums.length.
# Return the bitwise XOR of all elements of nums.

# Input: n = 4, start = 3
# Output: 8
# Explanation: Array nums is equal to [3, 5, 7, 9] where (3 ^ 5 ^ 7 ^ 9) = 8.
import operator
from functools import reduce


class Solution(object):
    def xorOperation(self, n, start):
        return reduce(operator.xor, [start+2*i for i in range(n)])


    if __name__ == '__main__':
        a = xorOperation(0,4,3)
        print(a)