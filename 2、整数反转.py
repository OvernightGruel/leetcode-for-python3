# 给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。
#
# 示例 1:
#
# 输入: 123
# 输出: 321
#  示例 2:
#
# 输入: -123
# 输出: -321
# 示例 3:
#
# 输入: 120
# 输出: 21
# 注意:
#
# 假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−231,  231 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。


class Solution:
    def reverse(self, x):
        x_str = str(x)
        x_list = list(x_str)
        a = None
        if x < 0:
            a = x_list.pop(0)
        x_reversed = reversed(x_list)
        x_str = ''.join(x_reversed)
        x_str = x_str.lstrip('0')
        if not x_str:
            return 0
        x_int = int(x_str)
        if x_int < 2 ** 31:
            x_int = 0 - x_int if a else x_int
            return x_int
        elif x_int == 2 ** 31 and a:
            return - 2 ** 31
        else:
            return 0


if __name__ == '__main__':
    s = Solution()
    s.reverse(123000)
