'''Реализация очереди c минимумом в Python'''
from math import inf

class Queue:
    def __init__(self):
        self.queue = []
        self.queueStart = 0
        self.queueMin = inf

    def push(self, val):
        self.queue.append(val)

    def pop(self):
        if len(self.queue) == 0:
            print("ERROR: current queue is empty")
            return None

        '''Передвигаем начало очереди, если неиспользуемых элем более половины удаляем их'''
        result = self.queue[self.queueStart]
        self.queueStart += 1
        if self.queueStart > len(self.queue) // 2:
            self.queue[:self.queueStart] = []
            self.queueStart = 0

        return result

    def top(self):
        return self.queue[0]

    def size(self):
        return len(self.queue)

    def isempty(self):
        return len(self.queue) == 0

    def clear(self):
        self.queue[:] = []
    def min_in_queue(self):
        if len(self.queue) > 0:
            return min(self.queue[self.queueStart:])

queue = Queue()
ans = []
colvo = 7
c = ['+ 1', '?', '+ 10', '?', '-', '?', '-']
for i in range(colvo):
    command = c[i]
    temp = command.split()
    com_type, num = temp[0], (temp[1] if len(temp) == 2 else None)
    if com_type == "+":
        queue.push(int(num))
    if com_type == "-":
       queue.pop()
    if com_type == "?":
      ans.append(queue.min_in_queue())


if len(ans) != 0:
    print(*ans)
