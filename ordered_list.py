class Node:
    '''Node for use with doubly-linked list'''
    def __init__(self, item):
        self.item = item
        self.next = None
        self.prev = None

class OrderedList:
    '''A doubly-linked ordered list of items, from lowest (head of list) to highest (tail of list)'''

    def __init__(self):
        '''Use ONE dummy node as described in class
           ***No other attributes***
           DO NOT have an attribute to keep track of size'''
        self.head = Node("Dumbo")
        self.head.next = self.head
        self.head.prev = self.head

    def is_empty(self):
        '''Returns True if OrderedList is empty
            MUST have O(1) performance'''
        if self.head.next is self.head:
            return True
        else:
            return False

    def add(self, item):
        '''Adds an item to OrderedList, in the proper location based on ordering of items
           from lowest (at head of list) to highest (at tail of list) and returns True.
           If the item is already in the list, do not add it again and return False.
           MUST have O(n) average-case performance'''
        pointer = self.head.next
        while pointer is not self.head:
            if item == pointer.item:
                return False
            if pointer.item > item:
                n = Node(item)
                n.next = pointer
                n.prev = pointer.prev
                pointer.prev = n
                n.prev.next = n
                return True
            pointer = pointer.next
        apnd = Node(item)
        apnd.next = self.head
        apnd.prev = self.head.prev
        self.head.prev.next = apnd
        self.head.prev = apnd
        return True

    def remove(self, item):
        '''Removes the first occurrence of an item from OrderedList. If item is removed (was in the list) 
          returns True.  If item was not removed (was not in the list) returns False
           MUST have O(n) average-case performance'''
        pointer = self.head.next
        while pointer is not self.head:
            if item == pointer.item:
                pointer.prev.next = pointer.next
                pointer.next.prev = pointer.prev
                return True
            pointer = pointer.next
        return False

    def index(self, item):
        '''Returns index of the first occurrence of an item in OrderedList (assuming head of list is index 0).
           If item is not in list, return None
           MUST have O(n) average-case performance'''
        i = 0
        pointer = self.head.next
        while pointer is not self.head:
            if item == pointer.item:
                return i
            pointer = pointer.next
            i += 1
        return None

    def pop(self, index):
        '''Removes and returns item at index (assuming head of list is index 0).
           If index is negative or >= size of list, raises IndexError
           MUST have O(n) average-case performance'''
        if index < 0:
            raise IndexError
        i = 0
        pointer = self.head.next
        while i < index:
            pointer = pointer.next
            i += 1
        if pointer == self.head:
            raise IndexError
        popval = pointer.item
        pointer.prev.next = pointer.next
        pointer.next.prev = pointer.prev
        return popval

    def search(self, item):
        '''Searches OrderedList for item, returns True if item is in list, False otherwise"
           To practice recursion, this method must call a RECURSIVE method that
           will search the list
           MUST have O(n) average-case performance'''
        return self.search_helper(item, self.head.next)

    def search_helper(self, item, lp):
        if lp.item == item:
            return True
        if lp.next is self.head:
            return False
        return self.search_helper(item, lp.next)

    def python_list(self):
        '''Return a Python list representation of OrderedList, from head to tail
           For example, list with integers 1, 2, and 3 would return [1, 2, 3]
           MUST have O(n) performance'''
        res = []
        pointer = self.head.next
        while pointer is not self.head:
            res += [pointer.item]
            pointer = pointer.next
        return res

    def python_list_reversed(self):
        '''Return a Python list representation of OrderedList, from tail to head, using recursion
           For example, list with integers 1, 2, and 3 would return [3, 2, 1]
           To practice recursion, this method must call a RECURSIVE method that
           will return a reversed list
           MUST have O(n) performance'''
        return self.rev_list_helper(self.head.prev)

    def rev_list_helper(self, lp):
        if lp is self.head:
           return []
        return [lp.item] + self.rev_list_helper(lp.prev)

    def size(self):
        '''Returns number of items in the OrderedList
           To practice recursion, this method must call a RECURSIVE method that
           will count and return the number of items in the list
           MUST have O(n) performance'''
        return self.size_helper(self.head.next)

    def size_helper(self, lp):
        if lp is self.head:
            return 0
        return 1 + self.size_helper(lp.next)

