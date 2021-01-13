"""
Given a sorted array (in ascending order) of integers and a target, write a function that finds the two integers that add up to the target.

Examples:

csSortedTwoSum([3,8,12,16], 11) -> [0,1]
csSortedTwoSum([3,4,5], 8) -> [0,2]
csSortedTwoSum([0,1], 1) -> [0,1]
Notes:

Each input will have exactly one solution.
You may not use the same element twice.
[execution time limit] 4 seconds (py3)

[input] array.integer numbers

[input] integer target

[output] array.integer
"""


def cs_sorted_two_sum(numbers, target):
    numbers.sort()
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == target:
                print(numbers[i], numbers[j], target)
                return [i, j]


def two_sum_faster(arr, target):
    nums = {}
    for num in arr:
        potential_match = target - num
        if potential_match in nums:
            return [potential_match, num]

        else:
            nums[num] = True

    return []

# print(two_sum([2, 5, 9, 13], 7))
# print(two_sum([4, 3, 5], 8))
