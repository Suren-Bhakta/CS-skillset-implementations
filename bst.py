

#  File: TestBinaryTree.py

#  Description: Creates Binary tree with given methods

#  Student Name: Suren Bhakta

#  Student UT EID: ssb2943

#  Partner Name:

#  Partner UT EID:

#  Course Name: CS 313E

#  Unique Number:

#  Date Created:

#  Date Last Modified:


import sys


class Node (object):
    # constructor
    def __init__(self, data):
        self.data = data
        self.lChild = None
        self.rChild = None

    def print_node(self, level=0):

        if self.lChild != None:
            self.lChild.print_node(level + 1)

        print(' ' * 3 * level + '->', self.data)

        if self.rChild != None:
            self.rChild.print_node(level + 1)

    def get_height(self):
        if self.lChild != None and self.rChild != None:
            return 1 + max(self.lChild.get_height(), self.rChild.get_height())
        elif self.lChild != None:
            return 1 + self.lChild.get_height()
        elif self.rChild != None:
            return 1 + self.rChild.get_height()
        else:
            return 1


class Tree(object):
    # constructor
    def __init__(self):
        self.root = None

    def print(self, level):
        self.root.print_node(level)

    def get_height(self):
        return self.root.get_height()

    # Inserts data into Binary Search Tree and creates a valid BST
    def insert(self, data):
        new_node = Node(data)
        if self.root == None:
            self.root = new_node
            return
        else:
            parent = self.root
            curr = self.root
            # finds location to insert new node
            while curr != None:
                parent = curr
                if data < curr.data:
                    curr = curr.lChild
                else:
                    curr = curr.rChild
            # inserts new node based on comparision to parent node
            if data < parent.data:
                parent.lChild = new_node
            else:
                parent.rChild = new_node
            return

    # Returns the range of values stored in a binary search tree of integers.
    # The range of values equals the maximum value in the binary search tree minus the minimum value.
    # If there is one value in the tree the range is 0. If the tree is empty the range is undefined.
    # For many of the the desired functions, helper methods were created
    def range(self):
        #Min and Max functions derived from professor github to fin min and max vals of tree
        min=Tree.minimum(self)
        max=Tree.maximum(self)
        range=max-min
        return(range)

    def minimum(self):
        current = self.root
        parent = current
        while (current != None):
            parent = current
            current = current.lChild
        return parent.data

    def maximum(self):
        current = self.root
        parent = current
        while (current != None):
            parent = current
            current = current.rChild
        return parent.data


    # Returns a list of nodes at a given level from left to right
    # Returns a list of nodes at a given level from left to right
    def get_level(self, level):
        return self.get_level_helper(self.root,level)

    # Helper method that calculates the list of nodes at a level
    def get_level_helper(self,nodeVal,level):
        if nodeVal== None:
            return [] # Returns empty list in the event of no nodes on level
        if nodeVal!= None:
            if level==0:
                return [nodeVal] # Returns root
            else:
               return self.get_level_helper(nodeVal.lChild,level-1) + self.get_level_helper(nodeVal.rChild,level-1)
            # This else statement all the left and right childs on concurrent level

    # Returns the list of the node that you see from left side
    # The order of the output should be from top to down
    def left_side_view(self):
        return self.left_side_view_helper(self.root)

    # Helper method that calculates the left side view
    def left_side_view_helper(self,node):
        finalList=[]
        if node==None:
            return [] # Returns empty list if no vals present in left side
        for level in range(0,self.root.get_height()): # Read the height off tree to set boundry for traversal of tree
            finalList.append(self.get_level(level)[0].data)  # Using the level function, get the level then only the left of the tree on each level
        return finalList

    # returns the sum of the value of all leaves.
    # a leaf node does not have any children.
    # returns the sum of the value of all leaves.
    # a leaf node does not have any children.
    def sum_leaf_nodes(self):
        return self.leaf_helper(self.root)

    # helper method that actually calculates the value of all leave nodes.
    def leaf_helper(self,node):
        sum=0
        if node==None:
            return 0
        if node.lChild is None and node.rChild is None: # Checks to see if the left and right nodes are leafs or not
            sum+=node.data
            return sum
        else:
            return self.leaf_helper(node.lChild)+self.leaf_helper(node.rChild)

def make_tree(data):
    tree = Tree()
    for d in data:
        tree.insert(d)
    return tree


# Develop your own main function or test cases to be able to develop.
# Our tests on the Gradescop will import your classes and call the methods.

def main():
    # Create three trees - two are the same and the third is different
    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    tree1_input = list(map(int, line)) 	# converts elements into ints
    t1 = make_tree(tree1_input)
    t1.print(t1.get_height())

    print("Tree range is: ",   t1.range())
    print("Tree left side view is: ", t1.left_side_view())
    print("Sum of leaf nodes is: ", t1.sum_leaf_nodes())
    print("##########################")

# Another Tree for test.
    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    tree2_input = list(map(int, line)) 	# converts elements into ints
    t2 = make_tree(tree2_input)
    t2.print(t2.get_height())

    print("Tree range is: ",   t2.range())
    print("Tree left side view is: ", t2.left_side_view())
    print("Sum of leaf nodes is: ", t2.sum_leaf_nodes())
    print("##########################")
# Another Tree
    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    tree3_input = list(map(int, line)) 	# converts elements into ints
    t3 = make_tree(tree3_input)
    t3.print(t3.get_height())

    print("Tree range is: ",   t3.range())
    print("Tree left side view is: ", t3.left_side_view())
    print("Sum of leaf nodes is: ", t3.sum_leaf_nodes())
    print("##########################")




if __name__ == "__main__":
    main()



