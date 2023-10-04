nums = [0, 1, 0, 3, 12]

non_zero = 0
j = 0

while j <= len(nums) - 1:
    if nums[j] != 0:
        temp = nums[j]
        nums[j] = nums[non_zero]
        nums[non_zero] = temp

        non_zero += 1
    j += 1

print(nums)

# class Solution:
#     def moveZeroes(self, nums: List[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         non_zero = 0
#         j = 0
#
#         while j <= len(nums) - 1:
#             if nums[j] != 0:
#                 temp = nums[j]
#                 nums[j] = nums[non_zero]
#                 nums[non_zero] = temp
#
#                 non_zero += 1
#             j += 1