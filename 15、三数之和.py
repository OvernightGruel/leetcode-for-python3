# 给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。

# 注意：答案中不可以包含重复的三元组。

#  

# 示例：

# 给定数组 nums = [-1, 0, 1, 2, -1, -4]，

# 满足要求的三元组集合为：
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]

class Solution:
    def threeSum(self, nums):
        l = len(nums)
        if l < 3 :
            return []
        nums.sort()
        res = []
        for i in range(l):
            if nums[i] > 0:
                return res
            if i > 0 and nums[i-1] == nums[i]:
                continue
            L = i+1
            R = l-1
            while L < R:
                s = nums[L]+nums[R]+nums[i]
                if s < 0:
                    L += 1
                elif s > 0:
                    R -= 1
                else:
                    res.append((nums[L], nums[R], nums[i]))
                    while L < R and nums[L] == nums[L+1]:
                        L += 1
                    while L < R and nums[R] == nums[R-1]:
                        R -= 1
                    L += 1
                    R -= 1
        return res

nums = [-1, 0, 1, 2, -1, -4]
print(Solution().threeSum(nums))       