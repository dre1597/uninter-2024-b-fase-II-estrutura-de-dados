class BST:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
        if self.data is None:
            self.data = data
        else:
            if data < self.data:
                if self.left:
                    self.left.insert(data)
                else:
                    self.left = BST(data)
            else:
                if self.right:
                    self.right.insert(data)
                else:
                    self.right = BST(data)

    def in_level(self):
        current = self
        lst = []
        queue = []
        queue.insert(0, current)

        while len(queue) > 0:
            current = queue.pop()
            lst.append(current.data)
            if current.left:
                queue.insert(0, current.left)
            if current.right:
                queue.insert(0, current.right)

        return lst

    def in_order(self, lst):
        if self.left:
            self.left.in_order(lst)
        lst.append(self.data)
        if self.right:
            self.right.in_order(lst)
        return lst

    def pre_order(self, lst):
        lst.append(self.data)
        if self.left:
            self.left.pre_order(lst)
        if self.right:
            self.right.pre_order(lst)
        return lst

    def post_order(self, lst):
        if self.left:
            self.left.post_order(lst)
        if self.right:
            self.right.post_order(lst)
        lst.append(self.data)
        return lst

tree = BST()
tree.insert(10)
tree.insert(5)
tree.insert(15)
tree.insert(2)
tree.insert(7)
tree.insert(12)
tree.insert(17)
print(tree)
