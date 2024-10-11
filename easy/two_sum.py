# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

 

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]
 

# Constraints:

# 2 <= nums.length <= 104
# -109 <= nums[i] <= 109
# -109 <= target <= 109
# Only one valid answer exists.
 

# Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?

def two_sum(nums: list, target: int) -> list:
    # this is list len check
    if not (2 <= len(nums) <= 10000):
        return []
    
    # target check
    if not (-1000000000 <= target <= 1000000000):
        return []
    
    nums_dict = {}

    for i, num in enumerate(nums):

        # check num
        if not (-1000000000 <= num <= 1000000000):
            continue

        diff = target - num
        if diff in nums_dict:
            return [nums_dict[diff], i]
        nums_dict[num] = i

    return []
    

def main():
    numbers = [3, 2, 7, 6]
    indices = two_sum(numbers, 8)
    print(indices)

main()