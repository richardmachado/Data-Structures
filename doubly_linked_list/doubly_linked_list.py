#! =============================================================           
#!                  CLASS LISTNODE
#! =============================================================
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next
    
    def __del__(self):
        self.value = None
        # if both self.prev and self.next are none
            # nothing should happen and instead will be handled in the DLL to adjust head & Tail
        if (self.next == None) and (self.prev == None):
            pass
        # if self.prev == None 
            # set next.prev to none
            # set self.next to none
        elif (self.next) and (self.prev == None):
                self.next.prev = None
                self.next = None
        # if self.next == None 
            # set prev.next to none
            # set self.prev to None
        elif (self.prev) and (self.next == None):
            self.prev.next = None
            self.prev = None
        # if self.prev & self.next
            # set prev.next to next
            # set next.prev to prev
            # set the self.prev and next to none
        else:
            self.prev.next = self.next
            self.next.prev = self.prev
            self.prev = None
            self.next = None

#! =============================================================           
#!              CLASS DOUBLYLINKEDLIST
#! =============================================================

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
        # Create instance of ListNode with Value
        lNode = ListNode(value)
        # Increment the DLL length attribute
        self.length += 1
        # if DLL is empty
            # set head and tail to the new node instance
        if self.length == 1:
            self.head = lNode
            self.tail = lNode
        # if DLL is not empty
            # Set new node's next to current head
            # set head's prev to new node
            # set head to the new node
        else:
            lNode.next = self.head
            self.head.prev = lNode
            self.head = lNode
        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
#! =============================================================           
#!                  REMOVE_FROM_HEAD
#! =============================================================

    def remove_from_head(self):
        # store the value of the head
        curVal = self.head.value
        # decrement the length of the DLL
        self.length -= 1
        # delete the head
        # if head.next is not None
            # set head.next's prev to None
            # set head to head.next
        if self.head.next != None:
            self.head = self.head.next
            self.__del__()
        # else (if head.next is None)
            # set head to None
            # set tail to None
        else:
            self.head.__del__()
            self.head = None
            self.tail = None
        #return the value
        return curVal

        pass
            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
#! =============================================================           
#!                  ADD_TO_TAIL
#! =============================================================

    def add_to_tail(self, value):
        # Create instance of ListNode with Value
        lNode = ListNode(value)
        # Increment the DLL length attribute
        self.length += 1
        # if DLL is empty
            # set head and tail to the new node instance
        if self.length == 1:
            self.head = lNode
            self.tail = lNode
        # if DLL is not empty
            # Set new node's prev to current tail
            # set tail's next to new node
            # set tail to the new node
        else:
            lNode.prev = self.tail
            self.tail.next = lNode
            self.tail = lNode
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
#! =============================================================           
#!                 REMOVE_FROM_TAIL
#! =============================================================

    def remove_from_tail(self):
        # store the value of the tail
        curVal = self.tail.value
        # decrement the length of the DLL
        self.length -= 1
        # delete the tail
        # if tail.prev is not None
            # set tail.prev's next to None
            # set tail to tail.prev
        if self.tail.prev != None:
            self.tail = self.tail.prev
            self.__del__()
        # else (if tail.prev is None)
                # set head to None
                # set tail to None
        else:
            self.tail.__del__()
            self.head = None
            self.tail = None
        #return the value
        return curVal
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
#! =============================================================           
#!                  MOVE_TO_FRONT
#! =============================================================

    def move_to_front(self, node):
        #confirm that the node is not already at the head or that it is not the only item
        if self.head.next is not None and node is not self.head:
            # adjust tail if node is the tail
            if node is self.tail:
                self.tail = self.tail.prev
            # adjust length add node to head and delete node
            self.length -= 1
            self.add_to_head(node.value)
            node.__del__()
        # if node is head or there is only one item good to pass
        else:
            pass
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
#! =============================================================           
#!                  MOVE_TO_END
#! =============================================================

    def move_to_end(self, node):
        #confirm that the node is not already at the tail or that it is not the only item
        if self.head.next is not None and node is not self.tail:
            #adjust head if node is head
            if node is self.head:
                self.head = self.head.next
            # adjust length add node to tail and delete node
            self.add_to_tail(node.value)
            node.__del__()
            self.length -= 1  
        # if node is tail or there is only one item good to pass
        else:
            pass
        

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
#! =============================================================           
#!                  DELETE A NODE
#! =============================================================

    def delete(self, node):
        # if only one node del via adjusting head and tail
        if self.head.next is None:
            self.head = None
            self.tail = None
        else:
            #if node is head adjust head
            if node is self.head:
                self.head = node.next
            # if node is tail adjust tail
            elif node is self.tail:
                self.tail = node.prev
            # use del function
            node.__del__()
        # adjust length
        self.length -= 1

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
#! =============================================================           
#!                  GET_MAX
#! =============================================================
    def get_max(self):
        #set value and current node
        current = self.head.next
        maxVal = self.head.value
        #set while loop to go through the DLL
        while current is not None:
            #check if new value is larger than current and if so replace
            if current.value > maxVal:
                maxVal = current.value
            #reset current to move the loop
            current = current.next
        #return largest value
        return maxVal