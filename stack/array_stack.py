class Stack:
    '''
        Stack data structure implemented using python list.
        It has the following method
        2. push -> for adding elemnts to the stack object
        3. pop_stack -> for removing elements from the stack
        4. clear_stack -> for clearing elements in the stack
    '''
    def __init__(self, head=None):
        self.arr = []
        if head:
            self.arr.append(head)
    
    def pop_stack(self):
        if len(self.arr) == 0:
            return -1
        return self.arr.pop()
    
    def push(self, entry):
        self.arr.append(entry)
        return self.arr
    
    def clear_stack(self):
        self.arr.clear()
        return self.arr

    def length(self):
        return len(self.arr)
    
    def get(self, index):
        if index < self.length():
            return self.arr[index]
        else:
            raise IndexError('Index out of range.')
    
    def __add__(self, other):
        t = self.arr + other.arr
        s = Stack()
        for i in t:
            s.push(i)
        return s
    
    def __str__(self):
        return 'This is a stack object'