class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

    def __str__(self):
        return str(self.val)


class LinkList:
    def __init__(self):
        self.length = 0
        self.header = None

    def is_empty(self):
        return self.length == 0

    def clear(self):
        self.header = None
        self.length = 0

    def get_val_list(self):
        cur = self.header
        val_list = []
        while cur is not None:
            val_list.append(cur.val)
            cur = cur.next
        return val_list

    def check_index(self, index):
        if index < 0 or index >= self.length:
            raise Exception('index out of range')

    def check_node(self, node):
        if not isinstance(node, ListNode):
            raise Exception('must ListNode instance')

    def get_node(self, index):
        self.check_index(index)
        if index == 0:
            return self.header
        else:
            cur = self.header
            while index:
                cur = cur.next
                index -= 1
            return cur

    def update_node_val(self, index, val):
        node = self.get_node(index)
        node.val = val

    def insert_node(self, index, node):
        self.check_node(node)
        if index == 0:
            node.next = self.header
            self.header = node
        else:
            pre_node = self.get_node(index - 1)
            node.next = pre_node.next
            pre_node.next = node
        self.length += 1

    def delete_node(self, index):
        self.check_index(index)
        if self.is_empty():
            raise Exception('list is empty')
        if index == 0:
            self.header = self.header.next
        else:
            pre_node = self.get_node(index - 1)
            pre_node.next = pre_node.next.next
        self.length -= 1

    def append_node(self, node):
        self.check_node(node)
        if self.is_empty():
            self.header = node
        else:
            last_node = self.get_node(self.length - 1)
            last_node.next = node
        self.length += 1

    def __str__(self):
        print_list = self.get_val_list()
        return '->'.join(print_list) if print_list else str(None)


def build_list(iter_list):
    link_list = LinkList()
    if len(iter_list) == 0:
        return link_list
    header = ListNode(iter_list[0])
    link_list.length = 1
    cur = header
    for v in iter_list[1:]:
        cur.next = ListNode(v)
        cur = cur.next
        link_list.length += 1
    link_list.header = header
    return link_list


if __name__ == '__main__':
    l = ['a', 'b', 'c']
    link_list = build_list(l)
    print(link_list)
    print(link_list.length)
    # print(link_list.get_node(0))
    # link_list.update_node_val(0, 'new')
    # print(link_list.get_node(0))
    # print(link_list)
    # link_list.insert_node(1, ListNode('in'))
    # print(link_list)
    # print(link_list.length)
    # link_list.append_node(ListNode('append'))
    # print(link_list)
    # print(link_list.length)
    link_list.delete_node(2)
    print(link_list)
    print(link_list.length)
