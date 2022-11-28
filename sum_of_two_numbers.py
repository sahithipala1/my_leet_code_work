# Given an array of integers nums and an integer target,
# return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.
from typing import List


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


if __name__ == "__main__":
    input_list = [1, 2, 3]
    target = 5
    
    answer = Solution().twoSum(nums=input_list, target=target)
    print(answer)
