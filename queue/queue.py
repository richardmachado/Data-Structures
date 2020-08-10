import sys
"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 
1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
"""
# https://techdifferences.com/difference-between-stack-and-queue.html 


# class Queue:
#     def __init__(self):
#         self.size = 0
#         self.total = 0
#         self.storage = []
    
#     def __len__(self):
#         return len(self.storage)

#     def enqueue(self, value):
#         self.storage.append(value)

#     def dequeue(self):
#         if len(self.storage) < 1:
#             return None
#         else:
#             return self.storage.pop(0)


# line = Queue()

# line.enqueue(1)
# line.enqueue(3)
# line.enqueue(1)
# line.enqueue(3)
# line.dequeue()

# print(line.storage)
# print(line.__len__())

# for each node

from doubly_linked_list import LinkedList

class Queue:
    # LIFO! Last in, first out
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

    def enqueue(self, value):
        self.size += 1
        self.storage.add_to_end(value)

    def dequeue(self):
        # 🐛 stack has no len?
        if self.size == 0:
            return None
        else:
            self.size -= 1
            return self.storage.remove_from_head()


stack = Queue()
stack.enqueue(1)
stack.enqueue(2)
stack.enqueue(3)
stack.enqueue(4)
stack.enqueue(5)
stack.enqueue(6)
stack.enqueue(7)
stack.dequeue()
stack.dequeue()
stack.dequeue()
stack.dequeue()



stack.__iter__()
print("Head:", stack.get_head())
print("Size:", stack.size)