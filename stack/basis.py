class Stack:
    def __init__(self):
        self.stack = []

    def pop(self):
        if self.is_empty():
            return None
        return self.stack.pop()

    def push(self, val):
        self.stack.append(val)

    def peak(self):
        if self.is_empty():
            return None
        return self.stack[-1]

    def size(self):
        return len(self.stack)

    def is_empty(self):
        return self.size() == 0


# 栈实现队列
class QueueByStack:
    def __init__(self):
        self.stack = Stack()
        self.stack_bak = Stack()

    def enqueue(self, val):
        self.stack.push(val)

    def dequeue(self):
        for i in range(self.stack.size()):
            val = self.stack.pop()
            self.stack_bak.push(val)
        res = self.stack_bak.pop()
        for j in range(self.stack_bak.size()):
            val = self.stack_bak.pop()
            self.stack.push(val)
        return res

# 堆实现栈

# 栈实现堆