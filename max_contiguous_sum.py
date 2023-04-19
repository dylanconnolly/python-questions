from typing import List

def max_contiguous_sum(nums: List[int]) -> int:
  subArraySum = 0
  # maxSum starts as first element in array
  maxSum = nums[0]
  
  for n in nums:
    # check if incoming sum is negative, 
    # if so we can toss that subArraySum out since
    # it will never contribute to maximizing the sum
    if subArraySum < 0:
      subArraySum = 0
    subArraySum += n
    maxSum = max(subArraySum, maxSum)

  return maxSum

print(max_contiguous_sum([1,-2,3,4,-5,6]))