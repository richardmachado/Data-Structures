from stack import Stack
from queue import Queue

"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

#! Terminology

#! Root  - the utmost node in a tree

#! Child - a node directly connected to another node when moving away from the root node

#! Parent - a node directly connected to another node when moving towards the root node

#! Siblings - Nodes that share the same parent are considered siblings

#! Leaf - A node that does not have any children on it's own

#! ================================================================

This part of the project comprises two days:
1. Implement the methods `insert`, `condef contains`, `get_max`, and `for_each` on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods on the BSTNode class.
"""
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        #? check if value is less than the current node's value
        if value < self.value:
            #? does the current node have a left child
            if self.left:
                self.left.insert(value)
            #? other wise , it doesn't have left child
            #? we can park the new node here
            else:
                self.left = BSTNode(value)

        #? otherwise the value is greater or equal to the current node's value
        else:
            #? does the current node have a right child?
            if self.right:
                #? if it does, call the right child's insert method to repeat the process
                self.right.insert(value)
            #? other wise , it doesn't have right child
            #? we can park the new node here            
            else:
                self.right = BSTNode(value)

#! ===============
#! CONTAINS
#! ===============

    #? Return True if the tree contains the value
    #? False if it does not
    def contains(self, target):
        #? if self.value is equal to target
        if self.value == target:
            return True
        #? if target is less than target
        elif target < self.value:
            #? is self.left is None, it isn't in the tree
            if self.left is None:
                return False
            #? if self.left is there then run recurson
            else:
                return self.left.contains(target)
        
        #? Otherwise
        else:
            if self.right is None:
                return False
            else:
                return self.right.contains(target)



#! ===============
#! GET_MAX
#! ===============



    # Return the maximum value found in the tree
    def get_max(self):
        #! iterative version 
        #? set a max val to be rewritten and a current for the loop
        maxVal = self.value
        current = self
        #? set up loop to rewrite max and continue loop
        while current is not None:
            maxVal = current.value
            current = current.right
        #? return final max
        return maxVal

        #! recursive version
        # if not self.right:
        #     return self.value
        # return self.right.get_max()

#! ===============
#! FOR_EACH
#! ===============    

    # Call the function `fn` on the value of each node
    #? i did iterative, recursive is below
    def for_each(self, fn):
        fn(self.value)
        #if there is a right run function on it
        if self.right:
            self.right.for_each(fn)
        # if there is a left run function on it
        if self.left:
            self.left.for_each(fn)

    #! Recursive
    #! call fn on self.value
    #? fn(self.value)
    #! check if self has a left child
    #? if self.left:
        #! call 'for_each' on the left child, passing the fn
        #? self.left.for_each(fn)
    #! check if self has right child
    #? if self.right:
        #! call 'for_each' on the right child, passing the fn
        #? self.right.for_each(fn)


    #! Depth-First Iterative - visits leaves first

    #! How do we achieve the same ordering that recursion gave us for free
    #! use a stack to achieve the same order
    #? stack =[]
    #! add the root node to our stack
    #? stack.append(self)
    
    #! continue popping from our stack so long as there are nodes in it
    #? while len(stack) > 0:
    #?     current_node = stack.pop()

        #! check if this node has children
        #? if current_node.right:
        #?    stack.append(current_node.right)
        #? if current_node.left:
        #?     stack.append(current_node.left)


#! breadth-first traversal - visits parents first
    #? from collections import deque
    #? q =  deque()
    #? q.append(self)
    
    #? while len(q) > 0:
        #? current_node = q.popleft()

        #! check if the node has childre
        #? if current_node.left:
            #? q.append(current_node.left)
        #? if current_node.right:
            #? q.append(current_node.right)

        #? fn(current_node.value)



    #! PART 2 - THURSDAY PROJECT

      



#! ===============
#! IN_ORDER_PRINT
#! ===============       

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        #? stack = []
        #? stack.append(self)
        
        #? if current node is None
        #? we know weve reached the end of a recursion 
        #? base case we want to return
        if self is None:
            return

        #? check if we can go left
        if self.left is not None:
            self.left.in_order_print(self)

        #? visit node by printing value
        print(self.value)

        #? now we check if we can go right
        if self.right is not None:
            self.right.in_order_print(self)

#! ===============
#! BFT_PRINT
#! ===============

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        #? use a queue to form a line for the nodes to get in line
        line = Queue()
        #? place the root in the queue
        line.enqueue(node)

        #? do a while loop to iterate
        #? while length of the queue is greater than 0
        while line.__len__() > 0:
            #? dequeue item from the queue
            val = line.dequeue()
            #? print the item
            print(val.value)

        #? place current item's left node in queue if not none
        if val.left:
            line.enqueue(val.left)
        #? place current item's right node in queue if not none
        if val.right:
            line.enqueue(val.right)

#! ===============
#! DFT_PRINT
#! ===============

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        #? initialize an empty stack
        line2 = Stack()
        #? push the root node onto the stack
        line2.push(node)

        #? need a while loop to manage interation
        #? if stack is not empty enter the while loop
        while line2.__len__() > 0:
            val = line2.pop()

        #? print the items value
        print(val.value)

        #? if right subtree
            #? push right item onto stack
        if val.right:
            line2.push(val.right)
        #? if left subtree
            #? push left item onto stack
        if val.left:
            line2.push(val.left)







#! ===============
#! STRETCH
#! =============== 
#     # Stretch Goals -------------------------
#     # Note: Research may be required

#     # Print Pre-order recursive DFT
#     def pre_order_dft(self, node):
#         pass

#     # Print Post-order recursive DFT
#     def post_order_dft(self, node):
#         pass
