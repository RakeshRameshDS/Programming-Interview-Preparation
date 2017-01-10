class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


root = Node(10)
L1 = Node(5)
L2 = Node(-3)
root.left = L1
root.right = L2
L3 = Node(3)
L4 = Node(2)
L5 = Node(11)
L1.left = L3
L1.right = L4
L2.right = L5
L6 = Node(3)
L7 = Node(-2)
L8 = Node(1)
L3.left = L6
L3.right = L7
L4.right = L8

res = []
def paths_to_sum(node, total, path):
    global res
    if node is None:
        return
    else:
        temp_path = [i for i in path]
        total -= node.data
        if total == 0:
            res.append(temp_path)
        temp_path.append(node.data)
        paths_to_sum(node.left, total, temp_path)
        paths_to_sum(node.right, total, temp_path)

def count_number_of_paths(node, total):
    if node is None:
        return 0
    else:
        res = 0
        total -= node.data
        if total == 0:
            res = 1
        l = count_number_of_paths(node.left, total)
        r = count_number_of_paths(node.right, total)
        return l+r+res

paths_to_sum(root, 18, [])
print(res)
print(count_number_of_paths(root, 18))