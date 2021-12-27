/*
 * Given an integer array nums, find the contiguous
 * subarray (containing at least one number) which has
 * the largest sum and return its sum.
 *
 * A subarray is a contiguous part of an array.
 * return all the possible permutations.
 */
# Solution 1: brute force (check sum for every subarray
def maxSubArray1(nums):
    maxSum = -inf
    for i in range(len(nums)):
        for j in range(i, len(nums)):
        currSum = 0
        for k in range(i, j+1):
            currSum += nums[k]
            maxSum = max(maxSum, currSum)

    return maxSum

# Solution 2: Kadane's algorithm
def maxSubArray2(nums):
    currSum, maxSum = 0, float('-inf')
    for n in nums:
        currSum += n
        maxSum = max(maxSum, currSum)
        if currSum < 0:
            currSum = 0
    return maxSum