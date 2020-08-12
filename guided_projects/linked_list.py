class Node:
    def __init__(self, value, next_node=None):
        #the value that the node is holding
        self.value = value
        #reference to the next node in the linked list
        self.next_node = next_node

    # method to get the value of the node

    def get_value(self):
        return self.value

    # method to get the nodes "next node"
    def get_next(self):
        return self.next_node

    #method to update the node's next node to the input node
    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_tail(self, value):
        #wrap the value in a node
        new_node = Node(value)
        #check if ll is empty
        if self.head is None and self.tail is None:
            #set head and tail to new node
            self.head = new_node
            self.tail = new_node
        #Otherwise, the list has at least 1 node
        else:
            # update the last node's 'next_node' to the new node
            self.tail.set_next(new_node)
            # update self.tail to point to the new node we just added
            self.tail = new_node

    def remove_tail(self):
        # check if linked list is empty
        if self.head is None and self.tail is None:
            return None
        
        # check if linked list has only 1 node
        if self.head == self.tail:
            val = self.head.get_value()
            self.head = None
            self.tail = None
            return val

        #otherwise, linked list has more than 1 value/
        else:
            #store the last nodes value to another variable to return it
            val = self.tail.get_value()
            #set 'self.tail' to be second-to-last node
            #the only way to do this is by traversing the whole list from the beginning

            #starting from the head, traverse to the second-to-last Node
            #init another reference ot keep track of where we are in the linked list as we're iterating
            current = self.head

            #keep iterating until node after 'current' is the tail
            while current.get_next() != self.tail:
                #keep iterating
                current = current.get_next()

            #set self.tail to 'current'
            self.tail = current
            #set new_tail next_node to None
            sef.tail.set_next(None)
            return val

    def remove_head(self):
        # check if the linked list is empty
        if self.head is None and self.tail is None:
            return None
        # store the old head's value that we need to return
        if self.head == self.tail:
            val = self.tail.get_value()
            self.head = None
            self.tail = None
        else:
        
            val = self.tail.get_value()
            # set self.head to old head's "next_node"
            self.head = self.head.get_next()
            # return the old head's value

    
ll = LinkedList()
ll.add_to_tail(5)

# ll = Node(5)
# ll.add_to_end(7)
# ll.add_to_end(18)
# ll.add_to_end(22)
# ll.set_next(Node(7))
# ll.next.set_next(Node(18))
# ll.next_node.next_node.set_next(Node(22))
# 11.next_node.next_node.next_node.set_next(Node(3))
