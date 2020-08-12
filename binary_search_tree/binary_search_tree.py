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
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each` on the BSTNode class.
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
        #? set a max val to be rewritten and a current for the loop
        maxVal = self.value
        current = self
        #? set up loop to rewrite max and continue loop
        while current is not None:
            maxVal = current.value
            current = current.right
        #? return final max
        return maxVal




#! ===============
#! FOR_EACH
#! ===============    

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        #if there is a right run function on it
        if self.right:
            self.right.for_each(fn)
        # if there is a left run function on it
        if self.left:
            self.left.for_each(fn)

            
    #! PART 2
#! ===============
#! IN_ORDER_PRINT
#! ===============             

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
