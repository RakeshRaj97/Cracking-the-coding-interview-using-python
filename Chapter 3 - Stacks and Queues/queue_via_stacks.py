# method to implement queue using two stacks
class QueueUsingStacks:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, item):
        self.stack1.append(item)

    def pop(self):
        while self.stack1:
            self.stack2 += [self.stack1.pop()]

        return self.stack2.pop()

    def peek(self):
        if self.stack1:
            return self.stack1[0]
        else:
            return self.stack2[-1]

if __name__ == "__main__":
    q = QueueUsingStacks()
    q.push(1)
    q.push(2)
    q.push(3)
    q.push(4)
    value = q.pop()
    print(value)
    value = q.peek()
    print(value)