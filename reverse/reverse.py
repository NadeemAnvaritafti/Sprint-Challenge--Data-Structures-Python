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

    def reverse_list(self, node, prev):
        # You must use recursion for this solution
        # if the list is empty, return None
        if not node:
            return
        # if the next node is None (then we know we're at the tail node)
        # make the head that node
        # make the next node now the previous 
        # -- once we get to the end, now we go back and switch all the pointers basically
        # 1 is head, None is previous; then 2 with 1 as its previous etc
        if node.next_node is None: 
            self.head = node  
            node.next_node = prev 
            return 
        # next = the next node
        # next node is now the previous
        # recursion: do the same thing with each node in the list
        next_one = node.next_node
        node.next_node = prev 
        self.reverse_list(next_one, node)
