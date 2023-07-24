class Queue:
    def __init__(self):
        self.queue = []
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def push(self, value):
        self.queue.append(value)
        self.size += 1

    def pop(self):
        if self.is_empty():
            raise Exception('Popping empty queue is not allowed')
        remove = self.queue[0]
        self.queue.pop(0)
        self.size += 1
        return remove

    def get_size(self):
        return self.size

    def __str__(self):
        output = ''
        for i in self.queue:
            output += str(i) + '->'
        return output[:-2]


if __name__ == '__main__':
    q = Queue()
    for i in range(10):
        q.push(i)
    q.pop()

    print(q)
        
