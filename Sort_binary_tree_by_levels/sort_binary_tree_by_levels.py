class Node:
    def __init__(self, L, R, n):
        self.left = L
        self.right = R
        self.value = n

    def __repr__(self):
        return f'{self.value}'

def tree_by_levels(node: Node, counter = 0, output = None):
    if output is None:
        output = []
    if node is None:
        return []
    if len(output) <= counter:
        output.append([])
    output[counter].append(node.value)
    tree_by_levels(node.left, counter+1, output)
    tree_by_levels(node.right, counter+1, output)
    our_outp = []
    for el in output:
        our_outp += el
    return our_outp
