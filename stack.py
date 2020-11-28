""" Stack """

class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def getLast(self):
        return self.items[ len(self.items) - 1 ]

    def size(self):
        return len(self.items)


# Use stack

stackList = Stack()

print(stackList.isEmpty())
stackList.push(3)
print(stackList.getLast())
stackList.push('Cat')
stackList.push(True)


print(stackList.size())
print(stackList.isEmpty())

stackList.push(100)

print(stackList.pop())
print(stackList.pop())
print(stackList.size())
print(stackList.getLast())
