import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList


# queue == first in first out
# stack == first in last out

class Stack:
    def __init__(self):
        # self.size = 0
        # Why is our DLL a good choice to store our elements?
        # it is in essence a list we can use for our stack
        self.storage = DoublyLinkedList()

    def __str__(self):
        if self.storage.head is None and self.storage.tail is None:
            return "empty"
        curr_node = self.storage.head
        output = ""
        output += f'({curr_node.value})'
        while curr_node.next is not None:
            curr_node = curr_node.next
            output += f' <-> ({curr_node.value})'
        return output

    def push(self, value):
        #add item to head of stack, increase size by 1
        # self.storage.add_to_tail(value)
        self.storage.add_to_tail(value)
        # self.size += 1

    def pop(self):
        # if the stack contains an item, remove it from from the rear
        # if self.size > 0:
        #     self.size -= 1
            # self.storage.remove_from_tail()
        return self.storage.remove_from_tail()

    def len(self):
        return self.storage.length

# myStack = Stack()

# print("Adding 6")
# myStack.push(6)
# print(myStack)
# print("Adding 7")
# myStack.push(7)
# print(myStack)
# print("Adding 2")
# myStack.push(2)
# print(myStack)
# print("Adding 4")
# myStack.push(4)
# print(myStack)

# remVal = myStack.pop()
# print(f'Popped from tail: {remVal}')
# print(myStack)

# print(f'Stack size now is at {myStack.len()}')