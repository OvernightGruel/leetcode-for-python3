from link_list.basis import ListNode, LinkList, build_list

# 头插法
def reverse_list(header):
    new_header = ListNode('new_header')
    while header:
        next_header = header.next
        header.next = new_header.next
        new_header.next = header
        header = next_header
    return new_header.next


l = ['a', 'b', 'c']
link_list = build_list(l)
new_header = reverse_list(link_list.header)
new_link = LinkList()
new_link.header = new_header
print(new_link)