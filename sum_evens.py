from typing import List

def sum_evens(nums: List[int]) -> int:
  return sum(filter(lambda n: not n%2, nums))

numList = range(11)

print(sum_evens(numList))