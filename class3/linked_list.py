class LinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data


class LinkedList:
    def __init__(self, nodes=None):
        self.head = None
        if nodes is not None:
            node = LinkedListNode(data=nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.next = LinkedListNode(data=elem)
                node = node.next

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

    def insert_first(self, node):
        node.next = self.head
        self.head = node

    def insert_last(self, node):
        if self.head is None:
            self.head = node
            return

        current = self.head

        while current.next:
            current = current.next

        current.next = node

