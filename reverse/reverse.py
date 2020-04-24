class Node:
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


class LinkedList:
    def __init__(self):
        # reference to the head of the list
        self.head = None

    def add_to_head(self, value):
        node = Node(value)
        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False
        # get a reference to the node we're currently at; update this as we
        # traverse the list
        current = self.head
        # check to see if we're at a valid node
        while current:
            # return True if the current value we're looking at matches our
            # target value
            if current.get_value() == value:
                return True
            # update our current node to the current node's next node
            current = current.get_next()
        # if we've gotten here, then the target node isn't in our list
        return False
    def print_list(self, head):
        tracker = head
        while tracker:
            if tracker:
                print(tracker.get_value())
            else:
                print(tracker)
            tracker = tracker.get_next()
    def reverse_list(self, node, prev):
        # You must use recursion for this solution
        # print('printing list')
        # if prev:
        #     prev.print_list(prev.head)
        # node is the head of the old list
        # prev is the new list

        # if prev is null base case
            # make a new node with head of node
            # del head of node
            # reverse_list(node, prev)
        # if node is null end case
            # return prev
        # else middle cases
            # add head of node to prev's head
            # del head of node
            # reverse_list(node, prev)
        if node is None and prev is None:
            return None

        if prev is None:
            # print(node.value, prev)

            # print(node, prev)
            new_linked_list = LinkedList()
            new_linked_list.add_to_head(node.get_value())
            self.reverse_list(node.get_next(), new_linked_list)
        elif node is None:
            # print('last case')
            # print(node, prev)
            self.head = prev.head
            # self.print_list(self.head)
        else:
            # print(node.value, prev)

            prev.add_to_head(node.get_value())
            self.reverse_list(node.get_next(), prev)

        # pass

