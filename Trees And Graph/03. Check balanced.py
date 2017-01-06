"""

"""

class TNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

root = TNode(2)
L1 = TNode(3)
L2 = TNode(4)
L3 = TNode(5)
L4 = TNode(6)
L5 = TNode(7)
L6 = TNode(8)
root.left = L1
root.right = L2
L2.left = L3
L3.left = L4
L1.left = L5
L2.right = L6

"""
Tree Structure

                    2
                  /   \
                3       4
              /       /   \
            7       5      8
                  /
                6

"""

def check_balanced(node):
    if node is None:
        return 0
    left = check_balanced(node.left)
    right = check_balanced(node.right)
    print(left, right, node.data)
    if left == -9999 or right == -9999:
        return -9999
    elif abs(left-right) <= 1:
        return max(left, right)+1
    else:
        return -9999

res = check_balanced(root)
print(res)