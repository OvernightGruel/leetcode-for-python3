# 判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。
#
# 示例 1:
#
# 输入: 121
# 输出: true
# 示例 2:
#
# 输入: -121
# 输出: false
# 解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
# 示例 3:
#
# 输入: 10
# 输出: false
# 解释: 从右向左读, 为 01 。因此它不是一个回文数。

# 进阶:
# 你能不将整数转为字符串来解决这个问题吗？


# class Solution:
#     def is_alindrome(self, x):
#         if x < 0:
#             return False
#         elif x < 10:
#             return True
#         else:
#             x_str = str(x)
#             if x_str.endswith('0'):
#                 return False
#             x_reversed = reversed(x_str)
#             reversed_x_str = ''.join(x_reversed)
#             if reversed_x_str == x_str:
#                 return True
#             else:
#                 return False


class Solution:
    def is_alindrome(self, x):
        if x < 0:
            return False
        elif x < 10:
            return True
        else:
            reverted_number = 0
            while x > reverted_number:
                reverted_number = x // 10 + reverted_number * 10
                x = x // 10
            return x == reverted_number or x == reverted_number // 10


if __name__ == '__main__':
    s = Solution()
    s.is_alindrome(121)