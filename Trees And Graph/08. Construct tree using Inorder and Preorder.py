class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

pre_order = ['A','B','D','E','C','F']
in_order =  ['D','B','E','A','C','F']

def pre_in_to_tree(pre_order, start_p, end_p, in_order, start_i, end_i):
    print(start_p, end_p, start_i, end_i)
    if start_i >= end_i or start_p >= end_p:
        return None
    root = pre_order[start_p]
    pos = -1
    for i in range(start_i, end_i):
        if in_order[i] == root:
            pos = i
            break
    print(root)
    res = Node(root)
    res.left = pre_in_to_tree(pre_order, start_p+1, pos+1, in_order, start_i, start_i + pos)
    res.right = pre_in_to_tree(pre_order, pos+1, end_p, in_order, start_i+pos+1, end_i)
    return res

pre_in_to_tree(pre_order, 0, len(pre_order), in_order, 0, len(in_order))