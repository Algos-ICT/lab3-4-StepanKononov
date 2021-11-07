'''Скобочная последовательность'''


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, val):
        self.stack.append(val)

    def pop(self):
        if len(self.stack) == 0:
            print("ERROR: current stack is empty")
            return None
        return self.stack.pop()

    def top(self):
        if len(self.stack) == 0:
            return None
        return self.stack[-1]

    def isempty(self):
        return len(self.stack) == 0

    def clear(self):
        self.stack[:] = []


num = int(input())

for i in range(num):
    subsequence = input()
    stack = Stack()
    for sym in subsequence:
        if stack.isempty():
            stack.push(sym)
        else:
            if stack.top() == '(' and sym == ')':
                stack.pop()
            if stack.top() == '[' and sym == ']':
                stack.pop()
            if (stack.top() == '(' or stack.top() == '[') and (sym == '(' or sym == '['):
                stack.push(sym)
    if stack.isempty():
        print('YES')
    else:
        print('NO')
