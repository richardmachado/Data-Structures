#! Terminology

#! Root  - the utmost node in a tree

#! Child - a node directly connected to another node when moving away from the root node

#! Parent - a node directly connected to another node when moving towards the root node

#! Siblings - Nodes that share the same parent are considered siblings

#! Leaf - A node that does not have any children on it's own

#! ================================================================

search rules

1. left child's value must be <  parent value 

2. right child's value must be > parent's value

what about duplicate values?

1. Now allow duplicate values in a BST(Binary Search Tree)

2. We will go with option 2. Pick a side, left or right, to also hold duplicate values

When searching a BST, We perform at most one comparison per level

Logarithmic runtime O(log2n)
Intuitively, you can think of it as "halving" the iteration space per iteration