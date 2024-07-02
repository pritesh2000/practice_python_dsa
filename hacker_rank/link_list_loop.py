# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        
        passed_node = set()

        while head:
            if head in passed_node:
                return True
            passed_node.add(head)
            head = head.next

        return False