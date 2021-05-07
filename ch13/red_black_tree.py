class NoSiblingError(Exception):
    pass


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

        while child.is_red and node.is_red:
            sibling = self._sibling(node)
            if sibling is not None and sibling.is_red:
                node.parent.left.is_red = False
                node.parent.right.is_red = False
                if node.parent != self.root:
                    node.parent.is_red = True
                node, child = node.parent.parent, node.parent
            else:
                self._rotate(node.parent, node, child)
                break

    def delete(self, key):
        pass

    def replace(self, key, value):
        pass

    def _sibling(self, node):
        if node == self.root:
            raise NoSiblingError('Current node is a root. No sibling for a root.')
        return node.parent.left if node == node.parent.right else node.parent.right

    def _rotate(self, g_parent, parent, child, new_child_is_red=True):
        # Parameter 'new_child_is_red' is designed to compatible for both insertion and deletion.
        # This parameter represents the children's color after rotation to be filled in.
        if not ((parent == g_parent.left and child == parent.left) or
                (parent == g_parent.right and child == parent.right)):
            is_right = child == parent.right
            self._relink(g_parent, child, not is_right)
            if is_right:
                self._relink(parent, child.left, is_right)
                self._relink(child, parent, not is_right)
            else:
                self._relink(parent, child.right, is_right)
                self._relink(child, parent, not is_right)
            parent, child = child, parent
        is_right = child == parent.right
        self._relink(g_parent.parent, parent, True if g_parent.parent and g_parent == g_parent.parent.right else False)
        self._relink(g_parent, parent.left, is_right)
        self._relink(parent, g_parent, not is_right)
        parent.is_red = g_parent.is_red
        g_parent.is_red = new_child_is_red
        child.is_red = new_child_is_red

    def _relink(self, parent, child, is_right):
        if parent:
            if is_right:
                parent.right = child
            else:
                parent.left = child
        else:
            self.root = child
        if child:
            child.parent = parent

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


if __name__ == '__main__':
    pass
