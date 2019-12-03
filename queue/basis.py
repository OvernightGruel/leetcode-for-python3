from link_list.basis import LinkList, ListNode, build_list


# python实现队列
class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, val):
        self.queue.append(val)

    def dequeue(self):
        if self.is_empty():
            return None
        return self.queue.pop(0)

    def is_empty(self):
        return self.size() == 0

    def size(self):
        return len(self.queue)

    def resever_val(self):
        for i in range(self.size() - 1):
            val = self.dequeue()
            self.enqueue(val)


# 队列实现栈
class StackByQueue:
    def __init__(self):
        self.queue = Queue()

    def push(self, val):
        self.queue.enqueue(val)

    def pop(self):
        self.queue.resever_val()
        return self.queue.dequeue()