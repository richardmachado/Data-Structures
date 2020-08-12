"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order.
1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when
   implementing a Stack?
"""
# for each node
from singly_linked_list import LinkedList

class Stack:
    # LIFO!
    def __init__(self):
        # size = len of list
        self.size = 0
        self.storage = LinkedList()
    
    def __len__(self):
        return self.size

    def __iter__(self):
        node = self.storage.head
        while node is not None:
            print(node.value)
            node = node.get_next()

    def get_head(self):
        return self.storage.head.get_value()

    def get_tail(self):
        return self.storage.tail.get_value()

    def push(self, value):
        self.size += 1
        self.storage.add_to_tail(value)

    def pop(self):
        # 🐛 stack has no len?
        if self.size == 0:
            return None
        else:
            self.size -= 1
            return self.storage.remove_tail()


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)
stack.push(6)
stack.push(7)
stack.pop()
stack.pop()
stack.pop()
stack.pop()



stack.__iter__()
print("Head:", stack.get_head())
print("Size:", stack.size)