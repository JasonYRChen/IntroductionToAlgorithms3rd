class BinaryTree:
    class _Node:
        __slots__ = 'key', 'value', 'parent', 'left', 'right'

        def __init__(self, key, value, parent=None, left=None, right=None):
            self.key = key
            self.value = value
            self.parent = parent
            self.left = left
            self.right = right

        def __repr__(self):
            return f"Node(k={self.key}, v={self.value}, p={self.parent.key if self.parent else None}, " \
                   f"l={self.left.key if self.left else None}, r={self.right.key if self.right else None})"

    def __init__(self):
        self.root = None
        self.size = 0

    def __repr__(self):
        for level, node in self._preorder():
            print('  '*level, node, sep='')
        return ''

    def __len__(self):
        return self.size

    def __getitem__(self, key):
        node = self.root
        while node:
            if node.key == key:
                return True, node
            if key < node.key and node.left:
                node = node.left
            elif key > node.key and node.right:
                node = node.right
            else:
                return False, node
        return False, node

    def __setitem__(self, key, value):
        is_node, node = self[key]
        if is_node:
            node.value = value
        else:
            if node:
                if key < node.key:
                    node.left = self._Node(key, value, node)
                else:
                    node.right = self._Node(key, value, node)
            else:
                self.root = self._Node(key, value)

    def __delitem__(self, key):
        is_node, node = self[key]
        if not is_node:
            raise KeyError(f'No such key {key}')
        self.delete(node)

    def delete(self, node):
        raise NotImplementedError

    def _preorder(self, node=None, level=0):
        if node is None:
            node = self.root
        yield level, node
        if node.left:
            yield from self._preorder(node.left, level+1)
        if node.right:
            yield from self._preorder(node.right, level+1)


def expectation(root_matrix, prob_array, dummy_array, row, col, depth=2):
    if row > col:
        return dummy_array[row] * depth
    root = root_matrix[row][col-row]
    return prob_array[root] * depth + \
        expectation(root_matrix, prob_array, dummy_array, row, root-1, depth+1) + \
        expectation(root_matrix, prob_array, dummy_array, root+1, col, depth+1)


def optimal_binary_search_tree_matrix(prob_array, dummy_array):
    inf = float('inf')
    length = len(prob_array)
    exps = [[inf] * length for _ in range(length)]
    roots = [[inf] * length for _ in range(length)]
    for diff in range(length):
        for start in range(length - diff):
            for root in range(start, start+diff+1):
                exp_left = expectation(roots, prob_array, dummy_array, start, root-1)
                exp_right = expectation(roots, prob_array, dummy_array, root+1, start+diff)
                exp = prob_array[root] + exp_left + exp_right
                if exp < exps[start][diff]:
                    exps[start][diff] = exp
                    roots[start][diff] = root
    return exps, roots


def optimal_binary_search_tree(prob_array, dummy_array):
    exps, roots = optimal_binary_search_tree_matrix(prob_array, dummy_array)
    to_analyze = [(0, len(prob_array)-1)]
    tree = BinaryTree()
    while to_analyze:
        start, end = to_analyze.pop()
        root = roots[start][end-start]
        tree[root] = prob_array[root]
        if start <= root - 1:
            to_analyze.append((start, root - 1))
        if end >= root + 1:
            to_analyze.append((root + 1, end))
    for i, dummy_prob in enumerate(dummy_array):
        tree[i-0.5] = dummy_prob
    return tree


if __name__ == '__main__':
    prob = [0.15, 0.1, 0.05, 0.1, 0.2]
    dummy = [0.05, 0.1, 0.05, 0.05, 0.05, 0.1]
    exps, roots = optimal_binary_search_tree_matrix(prob, dummy)
    print(exps)
    print(roots)
    # print(optimal_binary_search_tree(prob, dummy))
