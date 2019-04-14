# 编写一个函数来查找字符串数组中的最长公共前缀。
#
# 如果不存在公共前缀，返回空字符串 ""。
#
# 示例 1:
#
# 输入: ["flower","flow","flight"]
# 输出: "fl"
# 示例 2:
#
# 输入: ["dog","racecar","car"]
# 输出: ""
# 解释: 输入不存在公共前缀。
# 说明:
#
# 所有输入只包含小写字母 a-z 。


# class Solution:
#     def longest_common_prefix(self, strs):
#         start_str = ''
#         if not strs:
#             return start_str
#         elif len(strs) == 1:
#             return strs[0]
#         if '' in strs:
#             return start_str
#         len_list = list()
#         for s in strs:
#             len_s = len(s)
#             len_list.append(len_s)
#         min_len = min(len_list)
#         flag = True
#         for i in range(min_len):
#             if not flag:
#                 break
#             start_str = strs[0][:i + 1]
#             for s in strs:
#                 if not s.startswith(start_str):
#                     flag = False
#                     start_str = strs[0][:i]
#         return start_str

# class Solution:
#     def longest_common_prefix(self, strs):
#         if not strs:
#             return ""
#         s1 = min(strs)
#         s2 = max(strs)
#         for i, x in enumerate(s1):
#             if x != s2[i]:
#                 return s2[:i]
#         return s1

class Solution:
    def longest_common_prefix(self, strs):
        if not strs:
            return ""
        ss = list(map(set, zip(*strs)))
        res = ""
        for i, x in enumerate(ss):
            x = list(x)
            if len(x) > 1:
                break
            res = res + x[0]
        return res


if __name__ == '__main__':
    s = Solution()
    strs = ["flower", "flow", "flight"]
    result = s.longest_common_prefix(strs)
    print(result)
