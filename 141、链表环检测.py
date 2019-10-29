# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from link_list.basis import ListNode, LinkList, build_list


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        fast = slow = head
        while fast and slow and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow is fast:
                return True
        return False


a = ListNode('a')
b = ListNode('b')
c = ListNode('c')
d = ListNode('d')
e = ListNode('e')
a.next = b
b.next = c
c.next = d
d.next = e
e.next = c
has_cycle = Solution().hasCycle(a)
print(has_cycle)
