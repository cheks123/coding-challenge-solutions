class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.head = Node('head')
        self.size = 0

    def __str__(self):
        current = self.head.next
        output = ''
        while current:
            output += str(current.value) + '->'
            current = current.next
        return output[:-2]

    def is_empty(self):
        return self.size == 0

    def push(self, value):
        node = Node(value)
        node.next = self.head.next
        self.head.next = node
        self.size += 1

    def get_size(self):
        return self.size

    def pop(self):
        if self.is_empty():
            raise Exception('Popping from an empty stack.')
        remove = self.head.next
        self.head.next = self.head.next.next
        self.size -= 1
        return remove.value

    def mpop(self, n):
        if self.size < n:
            raise Exception (f'Cannot pop {n} from {self.size} items')
        for _ in range(n):
            self.pop()

if __name__ == '__main__':
    s = Stack()
    for i in range (1,11):
        s.push(i)

    print(s.get_size())
    print(s)
    s.mpop(11)
    print(s)

    
