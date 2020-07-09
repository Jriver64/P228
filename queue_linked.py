class Node:
    def __init__(self,item):
        self.item = item
        self.next = None

class Queue:
    '''Implements an link-based ,efficient first-in first-out Abstract Data Type'''

    def __init__(self, capacity):
        '''Creates an empty Queue with a capacity'''
        self.capacity = capacity
        n = Node(None)
        self.front = n
        self.back = n
        self.num_items = 0

    def is_empty(self):
        '''Returns True if the Queue is empty, and False otherwise'''
        if self.num_items == 0:
            return True
        return False

    def is_full(self):
        '''Returns True if the Queue is full, and False otherwise'''
        if self.num_items == self.capacity:
            return True
        return False

    def enqueue(self, item):
        '''If Queue is not full, enqueues (adds) item to Queue
           If Queue is full when enqueue is attempted, raises IndexError'''
        if 1 <= self.num_items < self.capacity:
            n = Node(item)
            n.next = None
            self.back.next = n
            self.back = n
            self.num_items += 1
        elif self.num_items == 0:
            self.front.item = item
            self.num_items += 1
        else:
            raise IndexError

    def dequeue(self):
        '''If Queue is not empty, dequeues (removes) item from Queue and returns item.
           If Queue is empty when dequeue is attempted, raises IndexError'''
        if self.capacity >= self.num_items > 0:
            item = self.front.item
            if self.front.next is not None:
                self.front = self.front.next
            self.num_items += -1
            return item
        else:
            raise IndexError


    def size(self):
        '''Returns the number of elements currently in the Queue, not the capacity'''
        return self.num_items
