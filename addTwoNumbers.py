# Given 2 non-empty linked lists that represent 2 non-negative numbers
# The digits are stored in reverse order
# each node contains a single digit
# Add the 2 numbers and return it as a linked list

# track carryover, set to variable = 0
# track current head = None
# track next item = None
# While there are elements in l1, l2, or carryover"
# call ListNone() and set to variable 'node'
# set val equal to value of l1 + l2 + carryover using getattr --> Takes in an obj, the name of the attribute, and default of 0 if not found


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1, l2):
        carryover = 0
        head = None
        nextItem = None

        while l1 or l2 or carryover:
            node = ListNode()
            val = getattr(l1, "val", 0) + getattr(l2, "val", 0) + carryover
            print("val", val)
            # assigns carryover of 1 if val is > 10 and node.val is set to 1s place 0 if carry over or the 1s place if not.
            carryover, node.val = divmod(val, 10)
            print("CO", carryover, 'node.val', node.val)

            # move head pointer if not none to next node
            if head is not None:
                nextItem.next = node
                nextItem = node
                print("nextItem", nextItem)
            else:
                print("node", node)
                # assign head and nextItem to node
                head = nextItem = node
                print('head', head)

            # grabs the next node if present and starts while loop again
            l1 = getattr(l1, "next")
            print('l1', l1)
            l2 = getattr(l2, "next")
            print('l2', l2)

        return head


# 2. Add Two Numbers
# Medium

# 8923

# 2250

# Add to List

# Share
# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Example:

# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.
