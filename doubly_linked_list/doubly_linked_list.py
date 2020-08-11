"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next
    
    def __del__(self):
        self.value = None

        #? what if self.prev and self.next are None
            #?return None
        if (self.next == None) and (self.prev == None):
            return None
            
        #?if self.prev == None
            #?set next.prev to none
            #? and set self.next to none
        elif (self.next) and (self.prev == None):
            self.next.prev = None
            self.next = None

        #? if self.next == None
            #?set prev.next to none
            #? and set self.prev to none
        elif (self.prev) and (self.next == None):
            self.prev.next = None
            self.prev = None

        #? if self.prev & self.next are the same
            #?set prev.next to next
            #? and set next.prev to prev
            #? and set the self.prev and next to none
        else:
            self.prev.next = self.next
            self.next.prev = self.prev
            self.prev = None
            self.next = None
            
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):

        #? create instance for ListNode with Value
        new_node = ListNode(value)

        #? increment the DLL length attribute
        self.length += 1
        
        #? of DLL is empty
            #? set head and tail to the new node instance
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
            
        #? if DLL is not empty
            #? set new node's next to current head
            #? set head's prev to new node
            #? set head to the new node

        else:
        #?update the locations of head and tails
            #? current head is being linked to new_head
            new_node.next = self.head
            #? updating old head to have a prev link
            self.head.prev = new_node
            #? updating new head to new node
            self.head = new_node
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        #?? store the value of the head
        curVal = self.head.value
        #?? decrement the lenght of the list
        self.length -= 1

        #?? delete the head
        #?? if head.next is ?= None
            #?? set head.next's prev to None
            #??set Head to head.next
        if head.next != None:
            self.head = self.head.next
            self.__del__()

        #? else if head.next is NOne
            #? set head to None
            #? set tail to None
        else:
            self.head.__del__()
            self.head = None
            self.tail = None

        #? return the value
        return curVal
    """

    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):

    #? create instance for ListNode with Value
        #? increment the DLL length attribute
        new_node = ListNode(value)
        #? INcrement the DLL value
        self.length += 1 
        #? of DLL is empty
            #? set head and tail to the new node instance
        if self.length == 1:
            self.head = new_node
            self.tail = new_node

        #? if DLL is not empty
            #? set new node's prev to current tail
            #? set tail's next to new node
            #? set tail to the new node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail= new_node
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):

        #? store the value of the tail
        curVal = self.head.value
        #? decrement the length of the DLL
        self.length -=1
        #? delete the tail
            #? if tail.prev is not None 
                #? set tail.prev's next to None
                #? set tail to tail.prev
        if self.tail.prev != None:
            self.tail = self.tail.prev
            self.__del__()
            #? else (if tail.prev is not None)
                #? set head to None
                #? set tail to None
        else:
            self.tail.__del__()
            self.head = None
            self.tail = None
        #? return the value 
        return curVal
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        #? confirm that the node is not already at head or not the only item
        if self.head.next is not None and node is not self.head:
            self.tail = self.tail.prev
            #? adjust the length add to node to head and delete node
            self.length -= 1
            self.add_to_head(node.value)
            node.__del__()
    #? if node is head or there is only 1 item, ok to pass
        else:
            pass
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        #? confirm the the node is not already at the tail or it is not the only item
        if self.head.next is not None and node is not self.tail:
            #? adjust head if node is head
            if node is self.head:
                self.head = self.head.next
            #? adjust length add not to tail and delete node
            self.add_to_tail(node.value)
            node.__del__()
            self.length -= 1
        #? if node is tail and there is only one it, just pass
        else:
            pass
    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        # if self.prev:
        #     self.prev.next = self.next #? node.prev.next = node.next
        # if self.next:
        #     self.next.prev = self.prev #? node.next.prev = node.prev
        if self.head.next is None:
            self.head = None
            self.tail = None
        else:
            if node is self.head:
                self.head = node.next
            elif node is self.tail:
                self.tail = node.prev
            node.__del__()
            self.length -= 1
            

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        #? set value and current node
        current = self.head.next
        maxVal = self.head.value

        #! while loop

        while current is not None:
            #? check if new value is larger than current
            if current.value > maxVal:
                maxVal = current.value
                #? reset current to to move the loop
            current = current.next
            #? return largest value
            return maxVal