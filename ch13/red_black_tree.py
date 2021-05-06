class RBTree:
    class _Node:
        __slots__ = 'key', 'value', 'parent', 'left', 'right', 'is_red'

        def __init__(self, key, value=None, parent=None, left=None, right=None, is_red=True):
            self.key = key
            self.value = value
            self.parent = parent
            self.left = left
            self.right = right
            self.is_red = is_red

    def __init__(self):
        self.size = 0
        self.root = None

    def __len__(self):
        return self.size

    def __repr__(self):
        k_v = [f"{node.key}:{node.value}" for node in self._inorder_list(self.root)]
        k_v = str(k_v)[1:-1]
        return f"RBTree({k_v})"

    def __getitem__(self, key):
        result, node = self.search(key)
        if result:
            return node.value
        raise KeyError('There is no such key.')

    def __setitem__(self, key, value):
        pass

    def __delitem__(self, key):
        pass

    def search(self, key):
        node = temp = self.root
        while temp is not None:
            if temp.key == key:
                return temp, temp

            node = temp
            if temp.key > key:
                temp = temp.left
            else:
                temp = temp.right
        return None, node

    def insert(self, key, value):
        if self.root is None:
            self.root = self._Node(key, value, is_red=False)
            return

        result, node = self.search(key)
        if result:
            raise KeyError(f'Key {key} already exist.')
        if key > node.key:
            node.right = self._Node(key, value, node)
            child = node.right
        else:
            node.left = self._Node(key, value, node)
            child = node.left

        while node.is_red:
            if node.parent.left.is_red and node.parent.right.is_red:
                node.parent.left.is_red = False
                node.parent.right.is_red = False
                if node.parent != self.root:
                    node.parent.is_red = True
                node = node.parent
            else:
                pass

    def delete(self, key):
        pass

    def replace(self, key, value):
        pass

    def _rotate(self, g_parent, parent, child):
        if not ((parent == g_parent.left and child == parent.left) or
                (parent == g_parent.right and child == parent.right)):
            is_right = child == parent.right

    def _relink(self, parent, child, is_right):
        pass

    def _preorder_list(self, node, level=0):
        yield level, node
        if node.left:
            yield from self._preorder_list(node.left, level+1)
        if node.right:
            yield from self._preorder_list(node.right, level+1)

    def _inorder_list(self, node):
        if node.left:
            yield from self._inorder_list(node.left)
        yield node
        if node.right:
            yield from self._inorder_list(node.right)
