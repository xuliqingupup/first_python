class Node():
    def __init__(self, data, lchild=None, rchild=None):
        self.data = data
        self.lchild = lchild
        self.rchild = rchild


class binaryTree():
    def __init__(self, root=None):
        self.root = root
        self.help_quene = []

    def build_tree(self, node: Node):
        if self.root is None:
            self.root = node
            self.help_quene.append(node)
        else:
            self.help_quene.append(node)
            if self.help_quene[0].lchild is None:
                self.help_quene[0].lchild = node
            else:
                self.help_quene[0].rchild = node
                self.help_quene.pop(0)

    def pre_order(self, current_node: Node):
        if current_node is not None:
            print(f'{current_node.data} ', end='')
            self.pre_order(current_node.lchild)
            self.pre_order(current_node.rchild)


if __name__ == '__main__':
    tree = binaryTree()
    for i in range(1, 11):
        new_node = Node(i)
        tree.build_tree(new_node)
    tree.pre_order(tree.root)
    print()
