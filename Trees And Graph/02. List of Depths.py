"""
Given a binary tree, design an algorithm which creates  linked list of all nodes at each depth
"""

class LLNode:
    def __init__(self, data):
        self.data = data
        self.link = None

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
root.left = L1
root.right = L2
L2.left = L3
L3.left = L4
L1.left = L5

"""
Tree Structure

                    2
                  /   \
                3       4
              /       /
            7       5
                  /
                6

"""
def listOfDepths(root):
    Q = []
    list_res = []; ll = []
    Q.append(root)
    Q.append(None)
    while Q is not None:
        ele = Q.pop(0)
        if ele is not None:
            ll.append(ele.data)
            if ele.left is not None: Q.append(ele.left)
            if ele.right is not None: Q.append(ele.right)
        else:
            if len(ll) == 0:
                break
            list_res.append(ll)
            ll = []
            Q.append(None)
    return list_res

LL = listOfDepths(root)
print(LL)
