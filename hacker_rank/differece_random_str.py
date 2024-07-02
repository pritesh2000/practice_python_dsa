class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# class MadeNode:
#     def __init__(self):
#         self.node = ListNode()

#     def add(self, data):

#         new_node = ListNode(data)
#         node = self.node
#         while node.next != None:
#             node = node.next
#         node.next = new_node

#     def display(self):

#         cur = self.node
#         dis = []
#         while cur.next != None:
#             cur = cur.next
#             dis.append(cur.val)
#         return dis


# l1 = MadeNode()
# l1.add(2)
# l1.add(4)
# l1.add(3)

# l2 = MadeNode()
# l2.add(5)
# l2.add(6)
# l2.add(4)

# list_1 = list_2 = []
# flag_1 = flag_2 = 0

# head = l1
# lhead = l2
# print(lhead.display())


# while head or lhead:
#     if head is None:        # head is None
#         if flag_1 == 0:
#             list_1.reverse()
#             flag_1 = 1
#         else:
#             list_1.append(0)
#     else:
#         list_1.append(head.val)

#     if lhead is None:       # lhead is None
#         if flag_2 == 0:
#             list_2.reverse()
#             flag_2 = 1
#         else:
#             list_2.append(0)
#     else:
#         list_2.append(lhead.val)

#     if len(list_1) == len(list_2):  # head and lhead have same length
#         if head is not None:
#             head = head.next
#         if lhead is not None:
#             lhead = lhead.next
