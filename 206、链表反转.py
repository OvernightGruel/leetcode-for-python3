# 反转一个单链表。
#
# 示例:
#
# 输入: 1->2->3->4->5->NULL
# 输出: 5->4->3->2->1->NULL

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from link_list.basis import ListNode, LinkList, build_list


class Solution:
    def reverseList(self, head):
        cur, pre = head, None
        while cur:
            cur.next, pre, cur = pre, cur, cur.next
        return pre


l = ['a', 'b', 'c', 'd']
link_list = build_list(l)
new_header = Solution().reverseList(link_list.header)
new_link = LinkList()
new_link.header = new_header
print(new_link)
