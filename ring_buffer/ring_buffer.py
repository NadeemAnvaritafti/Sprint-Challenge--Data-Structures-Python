from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        if self.storage.length < self.capacity:
            self.storage.add_to_tail(item)
            self.current = self.storage.head
            # least recently added is the current
        else:
            lru = self.storage.head
            self.storage.remove_from_head()
            self.storage.add_to_tail(item)
            if lru == self.current:
                self.current = self.storage.tail
        # self.current acts as a marker to indicate we've 
        # gone through the entire list and hit our lru

# self.current = 1
# lru = 1
# [1, 2, 3, 4, 5]


# [a, b, c, d]
# curr = a

# contents = [a, b, c, d]
# curr.next exists
# curr = a
# next_node = b
# add b
# next_node = c
# add c
# next_node = d
# add d
# next_node.next = None
# next_node = head = a
# next_node = curr ----> end loop
# add e to tail, then curr = a
# [a, b, c, d, e]
# add f:
#   --- remove head, add f to tail
#   --- [b, c, d, e, f]
#   --- curr is now f
# add f to contents array
# [f]
# curr.next == None (because f is at tail)
# next_node = head = b
# repeat until we get to e
# e.next = f 
# next_node = f = curr so our loop ends
# contents array should add f first, then next node will jump to the head
# and iterate starting from there adding each one to our contents array

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # First add self.current to contents array
        # then we'll find the next node and set our while loop to iterate starting from that point
        curr = self.current
        list_buffer_contents.append(curr.value)

        # if there is more than one node, then we'll set our next node for the loop
        if curr.next:
            next_node = curr.next
        else:
            next_node = self.storage.head

        # start at node after curr (REMEMBER curr is just a marker)
        # so then we'll add each node to our contents array until
        # we reach the end of the list (.next == None)
        # then we'll make 'next_node' equal to the head so that our loop ends
        # because now 'next_node' is the head and curr is also the head
        while next_node is not curr:
            list_buffer_contents.append(next_node.value)
            if next_node.next:
                next_node = next_node.next
            else:
                next_node = self.storage.head

        # curr = self.current
        # while curr:
        #     list_buffer_contents.append(curr.value)
        #     curr = curr.next

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
