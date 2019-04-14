# 给定 nums = [2, 7, 11, 15], target = 9
#
# 因为 nums[0] + nums[1] = 2 + 7 = 9
# 所以返回 [0, 1]


# class Solution:
#     def two_sum(self, nums, target):
#         for i in nums:
#             a = nums.index(i)
#             j = target - i
#             if j in nums:
#                 b = nums.index(j)
#                 if i == j:
#                     nums[a] = 'num_1'
#                     if j in nums:
#                         b = nums.index(j)
#                         return a, b
#                 else:
#                     return a, b


class Solution:
    def two_sum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap = {}
        for index, num in enumerate(nums):
            another_num = target - num
            if another_num in hashmap:
                return [hashmap[another_num], index]
            hashmap[num] = index
        return None
