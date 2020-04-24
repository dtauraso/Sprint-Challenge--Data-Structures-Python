import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList


class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # Modifying the order of elements is O(1) time, because they are not stored strictly in a sequence .

        self.storage = DoublyLinkedList()

    def enqueue(self, value):
        # push to front
        self.storage.add_to_head(value)
        self.size += 1
        # pass

    def dequeue(self):
        if(self.size == 0):
            return None
        old_value = self.storage.remove_from_tail()
        self.size -= 1
        return old_value
        # pass

    def len(self):
        return self.size
        # pass
