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
    def is_alindrome(self, n):
        if n < 0:
            return False
        elif n < 10:
            return True
        else:
            res = 0
            x = n
            while x != 0:
                x, y = divmod(x, 10)
                res = res * 10 + y
        return res == n


if __name__ == '__main__':
    s = Solution()
    print(s.is_alindrome(1223220))