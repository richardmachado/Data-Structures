# class LRUCache:
#     """
#     Our LRUCache class keeps track of the max number of nodes it
#     can hold, the current number of nodes it is holding, a doubly-
#     linked list that holds the key-value entries in the correct
#     order, as well as a storage dict that provides fast access
#     to every node stored in the cache.
#     """
#     def __init__(self, limit=10):
#         pass

#     """
#     Retrieves the value associated with the given key. Also
#     needs to move the key-value pair to the end of the order
#     such that the pair is considered most-recently used.
#     Returns the value associated with the key or None if the
#     key-value pair doesn't exist in the cache.
#     """
#     def get(self, key):
#         pass

#     """
#     Adds the given key-value pair to the cache. The newly-
#     added pair should be considered the most-recently used
#     entry in the cache. If the cache is already at max capacity
#     before this entry is added, then the oldest entry in the
#     cache needs to be removed to make room. Additionally, in the
#     case that the key already exists in the cache, we simply
#     want to overwrite the old value associated with the key with
#     the newly-specified value.
#     """
#     def set(self, key, value):
#         pass
import time

class Node:
    """
    Data:
    Stores two pieces of data:
    1. The Value
    2. The Next Node
    Methods/Behavior/Operations:
    1. Get value
    2. Set value
    3. Get next
    4. Set next
    """
    def __init__(self, value=None, next_node=None):
        # the value at this linked list node
        self.value = value
        # reference to the next node in the list
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        # set this node's next_node reference to the passed in node
        self.next_node = new_next


class LRUCache: 
    cache_limit = None
      
    # if the DEBUG is TRUE then it 
    # will execute 
    DEBUG = False
   
    def __init__(self, func): 
        self.func = func 
        self.cache = {} 
        self.head = Node(0, 0) 
        self.tail = Node(0, 0) 
        self.head.next = self.tail 
        self.tail.prev = self.head 
   
    def __call__(self, *args, **kwargs): 
          
        # The cache presents with the help 
        # of Linked List 
        if args in self.cache: 
            self.llist(args) 
              
            if self.DEBUG == True: 
                return f'Cached...{args}\n{self.cache[args]}\nCache: {self.cache}'
            return self.cache[args] 
   
        # The given cache keeps on moving. 
        if self.cache_limit is not None: 
              
            if len(self.cache) > self.cache_limit: 
                n = self.head.next
                self._remove(n) 
                del self.cache[n.key] 
   
        # Compute and cache and node to see whether  
        # the following element is present or not  
        # based on the given input. 
        result = self.func(*args, **kwargs) 
        self.cache[args] = result 
        node = Node(args, result) 
        self._add(node) 

        if self.DEBUG == True: 
            return f'{result}\nCache: {self.cache}'
        return result 
   
    # Remove from double linked-list - Node. 
    def _remove(self, node): 
        p = node.prev 
        n = node.next
        p.next = n 
        n.prev = p 
   
    # Add to double linked-list - Node. 
    def _add(self, node): 
        p = self.tail.prev 
        p.next = node 
        self.tail.prev = node 
        node.prev = p 
        node.next = self.tail 
   
    # Over here the result task is being done  
    def llist(self, args): 
        current = self.head 
          
        while True: 
              
            if current.key == args: 
                node = current 
                self._remove(node) 
                self._add(node) 
                  
                if self.DEBUG == True: 
                    del self.cache[node.key]   
                    self.cache[node.key] = node.val  
                break
              
            else: 
                current = current.next
   
   
# Default Debugging is FALSE. For  
# execution of DEBUG is set to TRUE 
LRUCache.DEBUG = True
   
# The DEFAULT test limit is NONE. 
LRUCache.cache_limit = 3
   
  
@LRUCache
def ex_func_01(n): 
    print(f'Computing...{n}') 
    time.sleep(1) 
    return n 
   
   
print(f'\nFunction: ex_func_01') 
print(ex_func_01(1)) 
print(ex_func_01(2)) 
print(ex_func_01(3)) 
print(ex_func_01(4)) 
print(ex_func_01(1)) 
print(ex_func_01(2)) 
print(ex_func_01(5)) 
print(ex_func_01(1)) 
print(ex_func_01(2)) 
print(ex_func_01(3)) 
print(ex_func_01(4)) 
print(ex_func_01(5)) 