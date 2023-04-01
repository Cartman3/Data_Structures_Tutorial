# A class to store a BST node
class Node:
    left = right = None

    # Function to create a new binary tree node having a given node_vlaue
    def __init__(self, data):
        self.data = data


# Function to perform sort in the tree
def sort_tree(xindex):

    if xindex is None:
        return

    sort_tree(xindex.left)
    print(xindex.data, end=' ')
    sort_tree(xindex.right)


# function to insert a vlaue into a BST
def insert(xindex, insert_value):

    # if the index is None, create a new node and return it
    if xindex is None:
        return Node(insert_value)

    # if the given value is less than the index node,
    # recur for the left subtree
    if insert_value < xindex.data:
        xindex.left = insert(xindex.left, insert_value)

    # otherwise, recur for the right subtree
    else:
        xindex.right = insert(xindex.right, insert_value)

    return xindex


# Function to construct a BST from given keys
def constructBST(insert_value):
    xindex = None
    for insert_value in insert_value:
        xindex = insert(xindex, insert_value)
    return xindex


#####################

    # Problem 1 #

#####################

# Write the code to make the BST sort the 'insert_values'. 
# You may change the variable names if you need.

if __name__ == '__main__':

    insert_value = [20, 12, 24, 7, 14, 18, 27]

    xindex = constructBST(insert_value)
    sort_tree(xindex)