def _find(self, root, value):
    if (root is None):
        return None
    if (value > root.value):
        self._find(root.right, value)
    elif (value < root.value):
        self._find(root.left, value)
    return value


def find(self, value):
    if (self.root is None):
        return None

    return self._find(self.root, value)
