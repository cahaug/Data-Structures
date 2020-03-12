"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    def __str__(self):
        if self.head is None and self.tail is None:
            return "empty"
        curr_node = self.head
        output = ''
        output += f'( {curr_node.value} ) <-> '
        while curr_node.next is not None:
            curr_node = curr_node.next
            output += f'( {curr_node.value} ) <-> '
        return output

    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""
    def add_to_head(self, value):
        # adding to an empty list
        new_node = ListNode(value)
        self.length += 1
        if self.head is None and self.tail is None:
            # create a new node
            new_node = ListNode(value)
            self.head = new_node
            self.tail = new_node
            # self.length += 1
        else:
            # adding a new value to existing list
            # link new_node with current head
            new_node.next = self.head
            self.head.prev = new_node
            # update head 
            self.head = new_node
            # self.length += 1

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""
    def remove_from_head(self):
        # if list is empty
        if self.head is None and self.tail is None:
            return 
        # if the head equals the tail, or if the length of the list is one, the list has only one element
        elif self.head == self.tail:
            #unlink the node
            value = self.head.value
            self.head = None
            self.tail = None
            self.length -= 1
            return value
        # if the list has multiple elements
        else:
            value = self.head.value
            next_head = self.head.next
            next_head.prev = None
            self.head.next = None
            self.head = next_head
            self.length -= 1
            return value

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""
    def add_to_tail(self, value):
        # adding to an empty list
        new_node = ListNode(value)
        self.length += 1
        if self.head is None and self.tail is None:
            # create a new node
            new_node = ListNode(value)
            self.head = new_node
            self.tail = new_node
        else:
            # adding a new value to existing list
            # link new_node with current head
            new_node.prev = self.tail
            self.tail.next = new_node
            # update head 
            self.tail = new_node

    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""
    def remove_from_tail(self):
        # if list is empty
        if self.head is None and self.tail is None:
            return 
        # if the head equals the tail, or if the length of the list is one, the list has only one element
        elif self.head == self.tail:
            #unlink the node
            value = self.head.value
            self.head = None
            self.tail = None
            self.length -= 1
            return value
        # if the list has multiple elements
        else:
            value = self.tail.value
            prev_tail = self.tail.prev
            prev_tail.next = None
            self.tail.prev = None
            self.tail = prev_tail
            self.length -= 1
            return value

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""
    def move_to_front(self, node):
        # if the list is empty
        # if self.head is None and self.tail is None:
        #     return
        # # if the head equals the tail/the length is one
        # elif self.head == self.tail:
        #     return
        # #if the list has multiple elements
        # else:
        #     value = node
        #     prev_node = node.prev
        #     print(prev_node)
        #     print(self.node)
        #     next_node = node.next
        #     print(next_node)
        #     prev_node.next = node.next
        #     next_node.prev = node.prev
        #     node.next = self.head
        #     self.head.prev = value
        #     # update head 
        #     self.head = value
        #     return
        pass
        

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""
    def move_to_end(self, node):
        pass

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""
    def delete(self, node):
        pass
        
    """Returns the highest value currently in the list"""
    def get_max(self):
        if self.head is None and self.tail is None:
            return "empty"
        curr_node = self.head
        highestValue = curr_node.value
        while curr_node.next is not None:
            if curr_node.value > highestValue:
                highestValue = curr_node.value
            curr_node = curr_node.next
        return highestValue

# our_dll = DoublyLinkedList()
# our_dll.add_to_head(6)
# our_dll.add_to_head(5)
# our_dll.add_to_head(13)
# print(f'our max value is: {our_dll.get_max()}')
# our_dll.remove_from_head()
# our_dll.add_to_head(5)
# our_dll.add_to_tail(7)

# print(our_dll)

# print(f'our max value is: {our_dll.get_max()}')