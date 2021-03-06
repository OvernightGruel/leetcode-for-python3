# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
#
# 有效字符串需满足：
#
# 左括号必须用相同类型的右括号闭合。
# 左括号必须以正确的顺序闭合。
# 注意空字符串可被认为是有效字符串。
#
# 示例 1:
#
# 输入: "()"
# 输出: true
# 示例 2:
#
# 输入: "()[]{}"
# 输出: true
# 示例 3:
#
# 输入: "(]"
# 输出: false
# 示例 4:
#
# 输入: "([)]"
# 输出: false
# 示例 5:
#
# 输入: "{[]}"
# 输出: true


class Solution:
    # def is_valid(self, s):
    #     while '{}' in s or '()' in s or '[]' in s:
    #         s = s.replace('{}', '')
    #         s = s.replace('[]', '')
    #         s = s.replace('()', '')
    #     return s == ''

    def is_valid(self, s):
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}
        for i in s:
            if i not in mapping:
                stack.append(i)
            elif mapping[i] != stack.pop() or not stack:
                return False
        return not stack




if __name__ == '__main__':
    s = Solution()
    result = s.is_valid('([)]')
    print(result)

