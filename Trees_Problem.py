#####################

    # Problem 1 #

#####################

# A class to store a BST node
class Node:
    left = right = None

    # Function to create a new binary tree node having a given node_vlaue
    def __init__(self, data):
        # Code goes here
        pass

# Function to perform sort in the tree
def sort_tree(xindex):

    # Code goes here
    pass

# function to insert a vlaue into a BST
def insert(xindex, insert_value):

    # if the index is None, create a new node and return it
    if xindex is None:
        return Node(insert_value)

    # if the given value is less than the index node,
    # recur for the left subtree
    
    # Code goes here

    # otherwise, recur for the right subtree
    pass


# Function to construct a BST from given keys
def constructBST(insert_value):
    xindex = None
    for insert_value in insert_value:
        xindex = insert(xindex, insert_value)
    return xindex

# Write the code to make the BST sort the 'insert_values'. 
# You may change the variable names if you need.

if __name__ == '__main__':

    insert_value = [20, 12, 24, 7, 14, 18, 27]

    xindex = constructBST(insert_value)
    sort_tree(xindex)