class Node:
    def __init__(self, value=None, nexxt=None):
        self.value = value
        self.next = nexxt

class LinkedList:
    '''
        LinkedList object

        METHODS
        is_empty -> returns boolean which tells whether the 
        linked-list is empty or not.
        
        push -> takes an argument and insert the argument at the beginning
        of the linked-list.
        
        pop -> removes and returns the item at the beginning of the linked-list
        
        get_list -> returns all the items in the linked-list separated by '->'
        
        get_size -> returns the number of items in the linked-list.
        
        insert -> takes position:int and item as argument and inserts the item
        at the position in the linked-list.
        
        insert_end -> inserts an item at the end of the linked-list.
        
        remove -> takes postion:int as argument remove the item at that position
        in the linked-list.
    
    '''
    def __init__(self):
        self.head = None
        self.size = 0

    def is_empty(self):
        '''
            This method tells whether the linked-list is empty or not.
        '''
        return self.size == 0
    
    def additem(self, value):
        '''
            This method inserts an item at the beginning of the linked-list.
        '''
        node = Node(value, self.head)
        self.head = node
        self.size += 1

    def pop(self):
        '''
            This method removes the item at the beginning of the the linked-list.
        '''
        if self.is_empty():
            raise Exception ('link-list is empty.')
        remove = self.head.value
        self.head = self.head.next
        self.size -= 1
        return remove
            

    def get_list(self):
        '''
        This method returns a string containing the items in the linked-list
        separated by '->'
        '''
        if self.is_empty():
            return '{}'
        current = self.head
        output = []

        for i in range(self.get_size()):
            output.append(current.value)
            current = current.next
        return '->'.join(map(str, output))
    def get_size(self):
        '''
            This method returns the number of items in the linked-list
        '''
        return self.size

    def insert(self, position, item):
        if position > self.get_size() + 1:
            raise Exception('Position out of range')
        current = self.head
        for i in range(position - 2):
            current = current.next
        nexxt = current.next
        node = Node(item)
        node.next = self.head
        self.head = node
        current.next = node
        self.size += 1
        
    def insert_end(self, item):
        '''
            This method inserts an item at the end of the linked list.
        '''
        self.insert(self.get_size() + 1, item)
    
    def remove(self, position):
        '''
        This position: int, as a parameter and removes the item from the 
        linked_list in the that position.
        '''
        if isinstance(position, int) == False:
            raise TypeError ('Position must be int.')
        if position > self.get_size() or position < 0:
            raise Exception('Position out of range')
        if position == 1:
            item = self.pop()
            return item
        current = self.head
        for i in range(position - 2):
            current = current.next
        nexxt = current.next.next
        current.next = nexxt
        self.size -= 1
    
    def get_item(self, position):
        if position > self.get_size():
            raise Exception('Position out of range')
        current = self.head
        for i in range(position - 1):
            current = current.next
        return current.value
            
        


    def __str__(self):
        if self.is_empty():
            return '{}'
        current = self.head
        output = []

        for i in range(self.get_size()):
            output.append(current.value)
            current = current.next
        r = '->'.join(map(str, output))
        return f'Linked-list object {r}'


if __name__ == '__main__':
    ll = LinkedList()
    for i in range(10):
        ll.additem(i)
    print(ll.get_size())
    print(ll.get_list())
    ll.insert(11, 1000)
    print(ll.get_list())
    ll.insert_end(999)
    print(ll.get_list())
    print(ll.get_size())
    print(ll.remove(1))
    print(ll.get_list())
    print(ll)
    
  
