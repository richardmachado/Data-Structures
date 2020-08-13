import sys

from singly_linked_list import LinkedList

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
        self.storage.add_to_tail(value)

    def dequeue(self):
        #  stack has no len?
        if self.size == 0:
            return None
        else:
            self.size -= 1
            return self.storage.remove_head()


# stack = Queue()
# stack.enqueue(1)
# stack.enqueue(2)
# stack.enqueue(3)
# stack.enqueue(4)
# stack.enqueue(5)
# stack.enqueue(6)
# stack.enqueue(7)
# stack.dequeue()
# stack.dequeue()
# stack.dequeue()
# stack.dequeue()



# stack.__iter__()
# print("Head:", stack.get_head())
# print("Size:", stack.size)