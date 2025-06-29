def maxSubArray(nums):

    maxSum = float('-inf')
    currSum = 0

    for i in range(len(nums)):
        currSum += nums[i]
        maxSum = max(maxSum, currSum)

        if currSum < 0:
            currSum = 0
    return maxSum

test = maxSubArray([1,2,3,4])
print(test)