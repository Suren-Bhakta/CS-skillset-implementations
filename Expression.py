import sys

operators = ['+', '-', '*', '/', '//', '%', '**']

# Given code which has the e operations of a stack and a function to check if the stack is empty
class Stack(object):
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if (not self.is_empty()):
            return self.stack.pop()
        else:
            return None

    def is_empty(self):
        return len(self.stack) == 0

# constructor
class Node(object):
    def __init__(self, data=None, lChild=None, rChild=None):
        self.data = data
        self.lChild = lChild
        self.rChild = rChild


class Tree(object):
    def __init__(self):
        self.root = None

    # this function takes in the input string expr and
    # creates the expression tree
    def create_tree(self, expr):
        expr = expr.split(' ')  # turning input into list and splitting char which will be used for ordering later
        sk = Stack()
        self.root = Node()
        current_node = self.root

        for char in expr:
            # after paranthesis a # will come so we can set it to left node to begin split
            if char == "(":
                current_node.lChild = Node()
                sk.push(current_node)
                current_node = current_node.lChild
            # If operator, push on stack, then set current node to right child
            elif char in operators:
                current_node.data = char
                sk.push(current_node)
                current_node.rChild = Node()
                current_node = current_node.rChild
            # If right parenthesis, checks to see if the list is empty
            elif char == ")":
                if len(sk.stack) != 0:
                    current_node = sk.pop()
            else:
                current_node.data = char  # when char is a number
                current_node = sk.pop()

    # this function should evaluate the tree's expression
    # returns the value of the expression after being calculated
    def evaluate(self, aNode):
    # include all operators in operator list to carry out functions
    # With the split list from create_tree, traverses through each function to check the operator and performs function
        if aNode.data == '**':
            return self.evaluate(aNode.lChild) ** self.evaluate(aNode.rChild)
        elif aNode.data == '*':
            return self.evaluate(aNode.lChild) * self.evaluate(aNode.rChild)
        elif aNode.data == '+':
            return self.evaluate(aNode.lChild) + self.evaluate(aNode.rChild)
        elif aNode.data == '-':
            return self.evaluate(aNode.lChild) - self.evaluate(aNode.rChild)
        elif aNode.data == '/':
            return self.evaluate(aNode.lChild) / self.evaluate(aNode.rChild)
        elif aNode.data == '%':
            return self.evaluate(aNode.lChild) % self.evaluate(aNode.rChild)
        elif aNode.data == '//':
            return self.evaluate(aNode.lChild) // self.evaluate(aNode.rChild)
        else:
            return float(aNode.data)

    # this function should generate the preorder notation of
    # the tree's expression
    # returns a string of the expression written in preorder notation
    def pre_order(self, aNode):
        # Use of empty string gets rid of error with none values with strip function in main
        new_str = ''
        if (aNode != None):
            new_str += aNode.data + ' '
            new_str += self.pre_order(aNode.lChild)
            new_str += self.pre_order(aNode.rChild)
        return new_str

    # this function should generate the postorder notation of
    # the tree's expression
    # returns a string of the expression written in postorder notation
    def post_order(self, aNode):
        # Use of empty string gets rid of error with none values with strip function in main
        new_str2 = ''
        if (aNode != None):
            new_str2 += self.post_order(aNode.lChild)
            new_str2 += self.post_order(aNode.rChild)
            new_str2 += aNode.data + ' '
        return new_str2


# you should NOT need to touch main, everything should be handled for you
def main():
    # read infix expression
    line = sys.stdin.readline()
    expr = line.strip()

    tree = Tree()
    tree.create_tree(expr)

    # evaluate the expression and print the result
    print(expr, "=", str(tree.evaluate(tree.root)))

    # get the prefix version of the expression and print
    print("Prefix Expression:", tree.pre_order(tree.root).strip())

    # get the postfix version of the expression and print
    print("Postfix Expression:", tree.post_order(tree.root).strip())


if __name__ == "__main__":
    main()
