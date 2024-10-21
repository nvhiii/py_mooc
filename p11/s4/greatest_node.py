# WRITE YOUR SOLUTION HERE:
class Node:
    """ Class is modeling single node in binary tree """
    def __init__(self, value, left_child:'Node' = None, right_child:'Node' = None):
        self.value = value
        self.left_child = left_child
        self.right_child = right_child

# Please write a function named greatest_node(root: Node) which takes the root node of a binary tree as its argument.

# The function should return the value of the node with the greatest value within the tree. The tree should be traversed recursively.

# Hint: the function sum_of_nodes in the example above may come in handy.

# An example of how the function should work:

# if __name__ == "__main__":
#     tree = Node(2)

#     tree.left_child = Node(3)
#     tree.left_child.left_child = Node(5)
#     tree.left_child.right_child = Node(8)

#     tree.right_child = Node(4)
#     tree.right_child.right_child = Node(11)

#     print(greatest_node(tree))

# 11

def greatest_node(root: "Node"):
    rn = root.value

    greatest_left_node = 0
    if not root.left_child is None:
        greatest_left_node = greatest_node(root.left_child)

    greatest_right_node = 0
    if not root.right_child is None:
        greatest_right_node = greatest_node(root.right_child)

    return max(rn, greatest_left_node, greatest_right_node)