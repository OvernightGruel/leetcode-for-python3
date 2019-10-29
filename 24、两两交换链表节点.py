# 给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。
#
# 你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
#
#  
#
# 示例:
#
# 给定 1->2->3->4, 你应该返回 2->1->4->3.

from link_list.basis import ListNode, LinkList, build_list


class Solution:
    def swapPairs(self, head):
        pre, pre.next = self, head
        while pre.next and pre.next.next:
            a = pre.next
            b = a.next
            pre.next, b.next, a.next = b, a, b.next
            pre = a
        return self.next


l = ['a', 'b', 'c', 'd']
link_list = build_list(l)
new_header = Solution().swapPairs(link_list.header)
new_link = LinkList()
new_link.header = new_header
print(new_link)
