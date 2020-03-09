from graphviz import Digraph


class Node:
    def __init__(self, id, label, parent=None, children=[]):
        self.id = id
        self.children = []
        self.parent = parent
        self.label = label
        for child in children:
            child_node = Node(child.children, self)
            self.children.append(child_node)

    def __repr__(self):
        return "Node: " + str(self.label)

    def __str__(self):
        return str(self.label)

    """
    Only Support Integers atm
    """
    def is_literal(self):
        try:
            int(self.label)
            return True
        except Exception:
            return False

    """
    TODO: Moet iteratief gemaakt worden
    """
    def only_literal_children(self):
        if not self.children:
            return self.is_literal()

        for child in self.children:
            if not child.only_literal_children():
                return False

        if len(self.children) == 1:
            self.label = self.children[0].label

        elif self.label == 'plus':
            self.label = 0
            for child in self.children:
                self.label += int(child.label)
        elif self.label == 'min':
            self.label = 0
            for child in self.children:
                self.label -= int(child.label)
        elif self.label == 'vm':
            self.label = 1
            for child in self.children:
                self.label *= int(child.label)
        elif self.label == 'deel':
            if int(self.children[1].label) == 0:
                return False
            self.label = int(self.children[0].label) / int(self.children[1].label)
        self.children = []
        return True

    def render_dot(self, graph=None):
        if graph is None:
            graph = Digraph(format='png')
        graph.node(str(self.id), str(self.label))

        if self.parent is not None:
            graph.edge(str(self.parent.id), str(self.id))

        for child in self.children:
            child.render_dot(graph)

        return graph

    def to_dot(self, file):
        if self.parent is None:
            file.write("digraph name {\n")

        file.write(str(self.id) + "[label=" + self.label + "] ;\n")
        if self.parent is not None:
            file.write(str(self.parent.id) + " -> " + str(self.id) + ";\n")

        for child in self.children:
            child.to_dot(file)

        if self.parent is None:
            file.write("}\n")


class Plus(Node):
    def __init__(self, children, parent=None):
        Node.__init__(self, children, parent)

    def toDot(self, file):
        file.write('plus')


class Min(Node):
    def __init__(self, children, parent):
        Node.__init__(children, parent)

    def toDot(self, file):
        file.write('min')


class ASTVisitor:
    def __init__(self, node):
        self.startnode = node

    def clean_tree(self):
        nodes = []
        queue = [self.startnode]
        # Get leaf nodes
        while len(queue) > 0:
            current_node = queue[0]

            queue = queue[1:]
            queue += current_node.children

            if len(current_node.children) == 1:
                index = current_node.parent.children.index(current_node)
                current_node.parent.children.remove(current_node)
                current_node.parent.children[index:index] = current_node.children
                current_node.children[0].parent = current_node.parent
                del current_node


    def constant_folding(self):
        nodes = [self.startnode]
        while len(nodes) > 0:
            current_node = nodes[0]
            nodes = nodes[1:]

            if current_node.label == "Bool1":
                current_node.only_literal_children()
            else:
                nodes += current_node.children
