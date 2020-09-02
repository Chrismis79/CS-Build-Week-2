# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
# Given a linked list of integers, remove any nodes from the linked list that have values that have previously occurred in the linked list. Your function should return a reference to the head of the updated linked list.

# Example:
# Input: (3) -> (4) -> (3) -> (2) -> (6) -> (1) -> (2) -> (6) -> N
# Output: (3) -> (4) -> (2) -> (6) -> (1) -> N
# Explanation: The input list contains redundant nodes(3), (6), and (2), so those should be removed from the list.

# [execution time limit] 4 seconds(py3)

# Planning: Need to loop over the linked list.
# node printed == ListNode with self.value and self.next
# Edge case: empty list
# Make a copy of the list
# loop though copy, make another copy inorder to be able to compare values
# nested while loop - while there is a next node
# if the value of the next node in the copied list is the same as the current value remove the node by changing the pointer to the next next node.
# otherwise move on and check the value of the next node by changing current and copied pointers.


def condense_linked_list(node):
    # node = ListNode class, if empty, return none
    if node is None:
        return None
    # Make pointer to the node and set variable to curr
    curr = node
    # while curr(node) is not empty
    while curr is not None:
        # make pointer to curr
        inner = curr
        # while there is a node next to the current node:
        while inner.next is not None:
            # if the value of the copy.next node is the same as the current node value
            if inner.next.value == curr.value:
                # change the next pointer to the node next to the next node (removing pointer to node, deletes the node)
                inner.next = inner.next.next
            # else move on and check the next node
            else:
                # move on to the next node and restart the loop
                inner = inner.next
        # move pointer to next node and start loop again
        curr = curr.next
    # return the new condensed list with duplicates removed.
    return node
 # Runtime O(n)
 # Space 0(n)

 # Improvements: Could have just tracked the current node, then looped through checking if the current node is the same as the visited node.
