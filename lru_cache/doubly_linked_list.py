"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next
   
    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev
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
    # """Wraps the given value in a ListNode and inserts it 
    # as the new head of the list. Don't forget to handle 
    # the old head node's previous pointer accordingly."""
    def add_to_head(self, value):
        # adding to an empty list
        new_node = ListNode(value)   
        self.length += 1
        if self.head is None and self.tail is None:
            # create a new node
            self.head = new_node
            self.tail = new_node
        else:
            # adding a new value, to existing list
            # link new_node with current head
            new_node.next = self.head
            self.head.prev = new_node
            # update head
    #         self.head = new_node
    # """Removes the List's current head node, making the
    # current head's next node the new head of the List.
    # Returns the value of the removed Node."""
    def remove_from_head(self):
        # if list is empty
        if self.head is None and self.tail is None:
            return  
        # if list has only one element
        elif self.head == self.tail:
            # unlink the node
            value = self.head.value
            self.head = None
            self.tail = None
            self.length -= 1
            return value
        else:
            # we have more than one element
            value = self.head.value
            next_head = self.head.next
            next_head.prev = None
            self.head.next = None
            self.head = next_head
            self.length -= 1
            return value
    # """Wraps the given value in a ListNode and inserts it 
    # as the new tail of the list. Don't forget to handle 
    # the old tail node's next pointer accordingly."""
    def add_to_tail(self, value):
        # adding to an empty list
        new_node = ListNode(value)   
        self.length += 1
        if self.head is None and self.tail is None:
            # create a new node
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
    # """Removes the List's current tail node, making the 
    # current tail's previous node the new tail of the List.
    # Returns the value of the removed Node."""
    def remove_from_tail(self):
       # if list is empty
        if self.head is None and self.tail is None:
            return  
        # if list has only one element
        elif self.head == self.tail:
            # unlink the node
            value = self.tail.value
            self.head = None
            self.tail = None
            self.length -= 1
            return value
        else:
            # we have more than one element
            value = self.tail.value
            prev_tail = self.tail.prev
            prev_tail.next = None
            self.tail.prev = None
            self.tail = prev_tail
            self.length -= 1
            return value
    # """Removes the input node from its current spot in the 
    # List and inserts it as the new head node of the List."""
    def move_to_front(self, node):
        if node is self.head:
            return 
        node_value = node.value
        # delete the node
        self.delete(node)
        self.add_to_head(node_value)
    # """Removes the input node from its current spot in the 
    # List and inserts it as the new tail node of the List."""
    def move_to_end(self, node):
        if node is self.tail:
            return 
        node_value = node.value
        # delete the node
        self.delete(node)
        self.add_to_tail(node_value)
    def delete(self, node):
        self.length -= 1
        if not self.head and not self.tail:
            return
        if self.head == self.tail:
            self.head = None
            self.tail = None
            return
        elif self.head == node:
            self.head = node.next
        elif self.tail == node:
            self.tail = node.prev
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev