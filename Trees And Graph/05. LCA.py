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

def LCA(root, n1, n2):
    if root is None:
        return None
    elif root == n1 or root == n2:
        return root
    else:
        left = LCA(root.left, n1, n2)
        right = LCA(root.right, n1, n2)
        if left and right:
            return root
        elif left:
            return left
        else:
            return right

res = LCA(root, L1, L3)
print(res.data)