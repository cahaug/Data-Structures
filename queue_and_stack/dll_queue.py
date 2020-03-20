import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList


# queue == first in first out
# stack == first in last out

class Queue:
    def __init__(self):
        # Why is our DLL a good choice to store our elements?
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

    def enqueue(self, value):
        # add to the rear of the list and reflect change in size
        self.storage.add_to_tail(value)

    def dequeue(self):
        # for queue take from front of queue, the head
        return self.storage.remove_from_head()

    def len(self):
        return self.storage.length

# testQueue = Queue()
# testQueue.enqueue(5)
# testQueue.enqueue(6)
# testQueue.enqueue(7)
# testQueue.enqueue(8)
# print(testQueue)
# print(f'Size of Queue: {testQueue.size}')
# remVal = testQueue.dequeue()
# print(f'Removed {remVal}')
# print(testQueue)

# print(f'Size of Queue: {testQueue.size}')