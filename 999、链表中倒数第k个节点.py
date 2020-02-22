# 输入一个链表，输出该链表中倒数第k个节点。
# 例如，一个链表有6个节点，从头节点开始，它们的值依次是1、2、3、4、5、6。这个链表的倒数第3个节点是值为4的节点。

# 示例：

# 给定一个链表: 1->2->3->4->5, 和 k = 2.

# 返回链表 4->5.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getKthFromEnd(self, head, k):
        fast = slow = head
        flag = 0
        while fast:
            fast = fast.next
            flag += 1
            if flag > k:
                slow = slow.next 
        return slow 
