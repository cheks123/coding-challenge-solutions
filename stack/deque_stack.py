from collections import deque

class Stack:
    def __init__(self, element=None):
        self.stack = deque()
        if element:
            self.stack.append(element)
    
    def add(self, element):
        self.stack.append(element)
        return self.stack
    
    def pop_stack(self):
        return self.stack.pop()
    
    def __len__(self):
        return len(self.stack)
    
    def __str__(self):
        return 'This is a Stack object implemented with python deque'
    
    def __repr__(self):
        return 'This is a Stack object'

    
