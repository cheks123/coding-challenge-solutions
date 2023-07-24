class TreeNode:
    def __init__(self, value):
        self.value = value
        self.less_child = None
        self.greater_child = None
        self.parent = None

class Tree:

    def find_parent(node, value):
        if node.value < value and node.greater_child == None:
            return node.less_child
        if node.value < value and node.greater_child != None:
            return find_parent(node.greater_child, value)
        if node.value > value and node.less_child == None:
            return node.less_child
        if node.value > value and node.less_child != None:
            return find_parent(node.less_child, value)
    
    def __init__(self, value):
        self.root = TreeNode(value)
        self.number_of_nodes = 1
    
    
    def add_node(self, value):

        def find_parent(node, value):
            if node.value <= value and node.greater_child == None:
                return node, 1
            if node.value <= value and node.greater_child != None:
                return find_parent(node.greater_child, value)
            if node.value > value and node.less_child == None:
                return node, 0
            if node.value > value and node.less_child != None:
                return find_parent(node.less_child, value)

        node = TreeNode(value)
        parent, kind = find_parent(self.root, value)
        node.parent = parent
        if kind == 1:
            parent.greater_child = node
        else:
            parent.less_child = node
        self.number_of_nodes += 1

    def node_count(self):
        return self.number_of_nodes

    def right_value(self):
        root = self.root
        root2 = self.root
        print(root.value)
        while root.greater_child:
            print(root.greater_child.value)
            root = root.greater_child
        
        while root2.less_child:
            print(root2.less_child.value)
            root2 = root2.less_child



if __name__ == '__main__':
    tree = Tree(4)
    for i in [6, 3, 5, 8, 4, 3]:
        tree.add_node(i)
    print(tree.node_count())
    tree.right_value()
    
