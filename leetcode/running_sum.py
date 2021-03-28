# 1480. Running Sum of 1d Array
# https://leetcode.com/problems/running-sum-of-1d-array/

# Input: nums = [1,2,3,4]
# Output: [1,3,6,10]
# Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].

def runningSum(self, nums):
    new_nums = list()
    for i in range(len(nums)):
        new_nums.insert(i, sum([nums[j] for j in range(i+1)]))
    print(new_nums)

if __name__ == '__main__':
    n = [1,2,3,4]
    runningSum(0,n)