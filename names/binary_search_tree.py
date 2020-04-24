import sys
# sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    def __str__(self):
        return f'{self.value}'
    # Insert the given value into the tree
    def insert(self, value):
        if self is None:
            return BinarySearchTree(value)
        # if the value is equal insert on the left
        elif value < self.value:
            if self.left:
                self.left.insert(value)
            else:
                self.left = BinarySearchTree(value)

        elif value >= self.value:
            if self.right:
                self.right.insert(value)
            else:
                self.right = BinarySearchTree(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # if self:
        #     print(self.value, target)
        if self is None:
            return False
          
        elif target < self.value:
            if self.left:
                return self.left.contains(target)
            else:
                return False

        elif target > self.value:
            # print('here')
            if self.right:
                return self.right.contains(target)
            else:
                return False

        elif target == self.value:
            return True
        # pass

    # Return the maximum value found in the tree
    def get_max(self):

        node = self
        max_ = 0
        if node:
            max_ = node.value

        my_stack = Stack()

        while my_stack.len() > 0 or node:
            # top = my_stack.pop()
            if node:
                my_stack.push(node)
                node = node.left
            else:
                node = my_stack.pop()
                # print(node.value)
                if(node.value > max_):
                    max_ = node.value
                node = node.right
        return max_
        # pass

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):

        # the root node is self
        node = self

        my_stack = Stack()

        while my_stack.len() > 0 or node:
            # top = my_stack.pop()
            if node:
                my_stack.push(node)
                node = node.left
            else:
                node = my_stack.pop()
                cb(node.value)
                node = node.right
        pass

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):

        if not node:
            return
        if node:
            self.in_order_print(node.left)
            print(node)
            self.in_order_print(node.right)


    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):

        my_queue = Queue()

        my_queue.enqueue(node)
        while(my_queue.len() > 0):
            tracker = my_queue.dequeue()
            print(tracker)
            # print(tracker.left, tracker.right)
            # print()

            if tracker.left:
                my_queue.enqueue(tracker.left)
            if tracker.right:
                my_queue.enqueue(tracker.right)

        # print('1\n8\n5\n7\n3\n6\n4\n2')
        # while queue exists
            # get head
            # if head is none
                # continue
            # print head
            
            # add head's children to end of queue

        # pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):

        # node is the tracker
        my_stack = Stack()

        while my_stack.len() > 0 or node:
            # if our tracker exists push it to stack and reassign it to the left
            if node:
                print(node)

                my_stack.push(node)
                node = node.left
            # if our tracker is null pop off from stack and use it for the tracker to visit the right
            else:
                node = my_stack.pop()
                node = node.right
            # print('stack start')
            # my_stack.Print()
            # print('stack end')

        # pass
    def make_spaces(self, number):
        if number == 0:
            return ''
        else:
            return ' ' + self.make_spaces(number - 1)


    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        if not node:
            return
        if node:
            print(node)
            self.pre_order_dft(node.left)
            self.pre_order_dft(node.right)
    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        if not node:
            return
        if node:
            self.post_order_dft(node.left)
            self.post_order_dft(node.right)
            print(node)


# x = BinarySearchTree(1)

# # x.insert(6)
# # x.insert(7)
# # x.insert(8)
# # x.insert(9)
# x.insert(8)
# x.insert(5)
# x.insert(7)
# x.insert(6)
# x.insert(3)
# x.insert(4)
# x.insert(2)

# tracker = x
# print()
# x.bft_print(tracker)

# # print('here')
