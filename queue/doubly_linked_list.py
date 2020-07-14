class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        # first node in list
        self.head = None
        # last node in list
        self.tail = None
    
    def add_to_end(self, value):
        # # regardless of if the list is empty or not, we need to wrap the value in a Node
        # new_node = Node(value)

        # # what if the list is empty?
        # if not self.head and not self.tail:
        #     self.head = new_node
        #     self.tail = new_node

        # else:
        #     # set the current tail's next to new node
        #     new_node.set_next(self.head)
        #     # set self.tail to new_node
        #     self.head = new_node
        new_node = Node(value)
        # what if the list is empty? 
        if not self.head:
            self.head = new_node
        # what if the list isn't empty?
        else:
            # what node do we want to add the new node to? 
            # the last node in the list 
            # we can get to the last node in the list by traversing it 
            current = self.head 
            while current.get_next() is not None:
                current = current.get_next()
            # we're at the end of the linked list 
            current.set_next(new_node)


        
    def remove_from_head(self):
        # what if the list is empty?
        if not self.head:
            return None

        else:
            # we want to return the value at the current head
            value = self.head.get_value()
            # remove the value at the head
            # update self.head
            self.head = self.head.get_next()
            return value
    
    def remove_tail(self):
        if not self.head:
            return None
        elif not self.head.get_next():
            return self.head.get_value()
        else:
            current = self.head
            while current.get_next():
            # navigate towards end of tail
                current = current.get_next()
                # current place
            node_to_del = current
            # value of current node
            node_to_del_val = current.get_value()

            current2 = self.head
            while current2.get_next() is not node_to_del:
                current2 = current2.get_next()
            current2.set_next(None)
            return node_to_del_val

