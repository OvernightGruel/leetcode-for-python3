# 给你两个有序整数数组nums1 和 nums2，请你将 nums2 合并到nums1中，使 nums1 成为一个有序数组。
#
# 说明:
#
# 初始化nums1 和 nums2 的元素数量分别为m 和 n 。
# 你可以假设nums1有足够的空间（空间大小大于或等于m + n）来保存 nums2 中的元素。
#
# 示例:
#
# 输入:
# nums1 = [1,2,3,0,0,0], m = 3
# nums2 = [2,5,6],       n = 3
#
# 输出:[1,2,2,3,5,6]


class Solution:
    def merge(self, nums1, nums2):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        n = 0
        for j in nums2:
            if n >= len(nums1)-1:
                nums1.append(j)
                n += 1
                continue
            for m in range(n, len(nums1)):
                i = nums1[m]
                if i > j:
                    nums1.insert(n, j)
                    n += 1
                    break
                else:
                    n += 1
            else:
                continue


nums1 = [1, 2, 3]
nums2 = [2, 5, 6]
s = Solution()
s.merge(nums1, nums2)
print(nums1)
print(nums2)
