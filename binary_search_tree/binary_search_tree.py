import sys
sys.path.append('../queue_and_stack')
# from dll_queue import Queue
# from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None #BinarySearchTree
        self.right = None  #BinarySearchTree

    # Insert the given value into the tree
    def insert(self, value):        
        if value < self.value and self.left is None:
            self.left = BinarySearchTree(value)
            return
        elif value >= self.value and self.right is None:
            self.right  = BinarySearchTree(value)
            return
        
        if value < self.value:
            self.left.insert(value)
        else:
            self.right.insert(value)
        # compare value to the current node
        # if smaller, go left
        # if larger, go right
        # if no node to go to, ie left or right is none
        # make a new node at that spot
        # pass

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # base case
        if target == self.value:
            return True
        # recursive cases
        if target < self.value:
            if self.left is None:
                return False
            return self.left.contains(target)
        if target > self.value:
            if self.right is None:
                return False
            return self.right.contains(target)
        # compare value to the current node value
        # if smaller, go left
        # if larger, go right
        # if equal, return True

        # if smaller, but we can't go left, return false
        # if larger, but we can't go right, return false


    # Return the maximum value found in the tree
    def get_max(self):
        # until right = none go right, return the final value
        if self.right is None:
            return self.value
        return self.right.get_max()

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        pass

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
