"""
Given a sorted array with unique integer elements, write an algorithm to create a binary search tree with minimal height
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def display_tree_inorder(node):
    if node is None:
        return
    else:
        display_tree_inorder(node.left)
        print(node.data," -> ", end='')
        display_tree_inorder(node.right)

arr = [1,2,3,4,5,6,7,8]

def minimal_tree(arr, start, end):
    if start > end:
        return None
    else:
        mid = int((start + end)/2)
        new_node = Node(arr[mid])
        new_node.left = minimal_tree(arr, start, mid-1)
        new_node.right = minimal_tree(arr, mid+1, end)
        return new_node

N = minimal_tree(arr, 0, len(arr)-1)
display_tree_inorder(N)