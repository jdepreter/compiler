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

    def render_dot(self, graph=None):
        if graph is None:
            graph = Digraph(format='png')
        graph.node(str(self.id), self.label)

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


class AST:
    def __init__(self, tree):
        self.startNode = Node(tree.children)

    def toDot(self):
        file = open('test.txt', 'w')
        self.startNode.toDot(file)
        file.close()
