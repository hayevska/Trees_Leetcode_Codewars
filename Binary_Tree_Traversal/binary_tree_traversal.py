class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def __repr__(self):
        return f'{self.data}'

# Pre-order traversal
def pre_order(node: Node):
    if node is None:
        return []
    output = [node.data]
    output += pre_order(node.left)
    output += pre_order(node.right)
    return output

# In-order traversal
def in_order(node: Node):
    if node is None:
        return []
    return in_order(node.left) + [node.data] + in_order(node.right)

# Post-order traversal
def post_order(node: Node):
    if node is None:
        return []
    return post_order(node.left) + post_order(node.right) + [node.data]
