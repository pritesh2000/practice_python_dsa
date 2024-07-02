class Node:
    def __init__(self, data = 0, next = None) -> None:
        self.data = data
        self.next = next

class FunNode:
    def __init__(self):
        self.node = Node()

    def node_length(self):

        curr = self.node
        l = 0
        while curr.next != None:
            l += 1
            curr = curr.next
        return l

    def append(self, data):

        new_node = Node(data)
        cur = self.node
        while cur.next != None:
            cur = cur.next
        cur.next = new_node

    def dislay(self):
        cur = self.node
        dis = []
        while cur.next!= None:
            cur = cur.next
            dis.append(cur.data)
        print(dis)


node1 = FunNode()
node1.append(2)
node1.append(3)

node1.node_length()
print(node1)
node1.dislay()
