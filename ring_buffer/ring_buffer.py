from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):

        # only true in the first round
        if len(self.storage) == 0:
            self.storage.add_to_head(item)
            self.current = self.storage.head

        # only true on the first pass after the first round
        elif len(self.storage) < self.capacity:
            self.storage.add_to_tail(item)
            self.current = self.storage.tail

        # only true on the remaining passes
        elif len(self.storage) == self.capacity:
            # print('current next', self.current.next)
            # at end of list
            if self.current.next is None:
                # print('wrap around case')
                self.storage.delete(self.storage.head)
                self.storage.add_to_head(item)
                self.current = self.storage.head

            # second to last
            elif self.current.next.next is None:
                # print('second to last case', item)
                self.storage.delete(self.current.next)
                self.storage.add_to_tail(item)
                # self.current.insert_after(item)
                self.current = self.storage.tail

                # print(self.current.value)
                # print(buffer.get())



            # third to last
            elif self.current.next.next is not None:
                # print('middle case', item)
                # print('current', self.current.value)
                # in the middle of list

                # curent_node delete_node next_node

                # hold the next next item
                temp = self.current.next.next
                # print('temp', temp.value)
                # print(buffer.get())
                # delete the next item
                self.storage.delete(self.current.next)
                # delete reduces the length but insert_after doesn't increase it
                self.storage.length += 1
                # print(buffer.get())

                self.current.insert_after(item)
                self.current = self.current.next

                # print('current now', self.current.value)
                # print('next now', self.current.next.value)

                # print('inserted new item')
                # print(buffer.get())
                # print('new current', self.current.value)
                # # self.current.next = temp
                # print(buffer.get())


            

        # pass

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here
        tracker = self.storage.head
        while tracker:
            list_buffer_contents.append(tracker.value)
            tracker = tracker.next
        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    # items are contiguously stored so all we have to do is modify the value

    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = [-1 for i in range(capacity)]

        pass

    def append(self, item):
        if self.current is None:
            self.current = 0
            self.storage[self.current] = item
        else:
            # rotate index
            self.current = (self.current + 1) % self.capacity

            self.storage[self.current] = item
        # pass

    def get(self):
        
        # print(self.storage)
        return [i for i in self.storage if i != -1]
        # pass


# buffer = RingBuffer(5)
# buffer.append('a')
# buffer.append('b')
# buffer.append('c')
# buffer.append('d')
# buffer.append('e')
# buffer.append('f')
# buffer.append('g')
# buffer.append('h')
# buffer.append('i')
# buffer.append('j')
# buffer.append('k')
# print('done')
# nodes = buffer.get()
# print(nodes)