nums = [1, 2, 3, 4, 5, 6, 7]
k = 4
# Output: [5,6,7,1,2,3,4]

l = len(nums)
temp = [0 for i in range(l)]
for i in range(l):
    index = ((i + k) % l)

    temp[index] = nums[i]

nums = temp
print(nums)

# class Solution:
#     def rotate(self, nums: List[int], k: int) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#
#         # l = len(nums)
#         # temp = [0 for i in range(l)]
#         # for i in range(l):
#         #     index = ((i + k) % l)
#         #     temp[index] = nums[i]
#
#         # nums=temp
#
#         k = k % len(nums)
#         n = len(nums) - k
#         nums[:] = nums[n:] + nums[:n]