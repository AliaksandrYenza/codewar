# https://leetcode.com/problems/can-make-arithmetic-progression-from-sequence/
# Given an array of numbers arr. A sequence of numbers is called an arithmetic progression
# if the difference between any two consecutive elements is the same.
# Return true if the array can be rearranged to form an arithmetic progression, otherwise, return false.
#
# Input: arr = [3,5,1]
# Output: true
# Explanation: We can reorder the elements as [1,3,5] or [5,3,1]
# with differences 2 and -2 respectively, between each consecutive elements.

class Solution(object):
    def canMakeArithmeticProgression(self, arr):
        arr = sorted(arr)
        dif = abs(arr[1] - arr[0])
        # print(f'dif = {dif}')
        if len(arr) <= 2:
            return True
        for i in range(len(arr)-1):
            # print(f'arr[{i}] + dif({dif}) = {arr[i]+dif} -> arr[{i+1} = {arr[i+1]}')
            if arr[i] + dif != arr[i+1]:
                return False
        return True

    if __name__ == '__main__':
        # arr = [13,12,-12,9,9,16,7,-10,-20,0,18,-1,-20,-10,-8,15,15,16,2,15]
        # arr = [1,2,4]
        arr = [3,5,1]
        f = canMakeArithmeticProgression(0,arr)
        print(f)



