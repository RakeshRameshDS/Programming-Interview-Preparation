"""

"""

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

root = Node(4)
L1 = Node(1)
L2 = Node(2)
L3 = Node(3)
L5 = Node(5)
L6 = Node(6)
L7 = Node(7)
root.left = L2
L2.left = L1
L2.right = L3
root.right = L6
L6.left = L5
L6.right = L7
'''
TREE

             4
           /    \
        2        6
      /    \   /   \
    1       3 5     7
'''


def validate(node, low, high):
    if node is None:
        return True
    if low <= node.data < high:
        left = validate(node.left, low, node.data)
        right = validate(node.right, node.data, high)
        if left and right:
            return True
        else:
            return False
    else:
        return False

print(validate(root, -9999999, 9999999))
