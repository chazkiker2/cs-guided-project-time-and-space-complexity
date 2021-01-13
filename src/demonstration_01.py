"""
Given an array of integers `numbers` and an integer `target`, return the indices
of the two numbers that add up to the `target`.

Examples:

- two_sum(numbers = [2,5,9,13], target = 7) -> [0,1] (numbers[0] + numbers[1] == 7)
- two_sum(numbers = [4,3,5], target = 8) -> [1,2] (numbers[1] + numbers[2] == 8)

Notes:

- Each input will have only one solution.
- You may not use the same element twice.
- You can return the answer in any order.
"""


def two_sum(nums, target):
    # Your code here
    nums.sort()
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                print(nums[i], nums[j], target)
                return [i, j]


print(two_sum([2, 5, 9, 13], 7))
print(two_sum([4, 3, 5], 8))
