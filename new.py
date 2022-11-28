from typing import List

import self as self


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[j] == target - nums[i]:
                    return [i, j]


if __name__ == "__main__":
    numbers = [1, 2, 3]
    target = 4
    
    answer = Solution.twoSum(self,nums=numbers, target=target)
    print(answer)
    
    
# solution 2

class Solution:
  def twoSum(self, nums: List[int], target: int) -> List[int]:
    print("sum of the two number")
    answer = []
    
    for i in range(len(nums)):
      for j in range(len(nums)):
        if (i != j) and (i < j) and (nums[i] + nums[j]) == target:
          answer.append(i)
          answer.append(j)
    
    return answer
