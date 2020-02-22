# 根据逆波兰表示法，求表达式的值。

# 有效的运算符包括 +, -, *, / 。每个运算对象可以是整数，也可以是另一个逆波兰表达式。

# 说明：

# 整数除法只保留整数部分。
# 给定逆波兰表达式总是有效的。换句话说，表达式总会得出有效数值且不存在除数为 0 的情况。
# 示例 1：

# 输入: ["2", "1", "+", "3", "*"]
# 输出: 9
# 解释: ((2 + 1) * 3) = 9
# 示例 2：

# 输入: ["4", "13", "5", "/", "+"]
# 输出: 6
# 解释: (4 + (13 / 5)) = 6
# 示例 3：

# 输入: ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
# 输出: 22
# 解释: 
#   ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
# = ((10 * (6 / (12 * -11))) + 17) + 5
# = ((10 * (6 / -132)) + 17) + 5
# = ((10 * 0) + 17) + 5
# = (0 + 17) + 5
# = 17 + 5
# = 22

from stack.basis import Stack
from queuee.basis import Queue

class Solution:
    def evalRPN(self, tokens):
        stack = list()
        for t in tokens:
            if t not in '+-*/':
                stack.append(int(t))
            else:
                right = stack.pop()
                left = stack.pop()
                if t == '+':
                    stack.append(left+right)
                elif t == '-':
                    stack.append(left-right)
                elif t == '*':
                    stack.append(left*right)
                elif t == '/':
                    stack.append(int(left/right))

        return stack[0]

tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
print(Solution().evalRPN(tokens))





