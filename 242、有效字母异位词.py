# 给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。

# 示例 1:

# 输入: s = "anagram", t = "nagaram"
# 输出: true
# 示例 2:

# 输入: s = "rat", t = "car"
# 输出: false

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap_s = {}
        hashmap_t = {}
        for i in s:
            hashmap_s[i] = hashmap_s.get(i, 0) + 1
        for j in t:
            hashmap_t[j] = hashmap_t.get(j, 0) + 1
        return hashmap_s == hashmap_t