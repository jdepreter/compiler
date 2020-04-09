from graphviz import Digraph
from src.helperfuncs import get_return_type


class Node:
    def __init__(self, node_id, node_type, label, parent, ctx):
        self.id = node_id
        self.children = []
        self.parent = parent
        self.label = label
        self.ctx = ctx
        self.symbol_table = None
        self.node_type = node_type
        self.symbol_type = None

    def __repr__(self):
        return "Node: " + str(self.label)

    def __str__(self):
        return str(self.label)

    """
    Only Support Integers atm
    """

    def is_literal(self):
        try:
            float(self.label)
            return True
        except Exception:
            return False

    """
    TODO: Moet iteratief gemaakt worden
    """

    def only_literal_children(self):
        if not self.children:
            return self.is_literal()

        fail = False
        for child in self.children:
            if not child.only_literal_children():
                fail = True

        if fail:
            return False

        # if len(self.children) == 1:
        #     self.label = self.children[0].label

        c0 = None
        c1 = None
        c0_type = self.children[0].symbol_type
        c1_type = self.children[1].symbol_type
        symbol_type = get_return_type(c0_type, c1_type)
        if '.' not in str(self.children[0].label):
            c0 = int(self.children[0].label)
        else:
            c0 = float(self.children[0].label)

        if '.' not in str(self.children[1].label):
            c1 = int(self.children[1].label)
        else:
            c1 = float(self.children[1].label)


        if self.node_type == '+':
            self.label = c0 + c1
        elif self.node_type == '-':
            self.label = c0 - c1
        elif self.node_type == '*':
            self.label = c0 * c1
        elif self.node_type == '/':
            if c1 == 0:
                raise ZeroDivisionError
            self.label = c0 / c1

        dic = {True: 1, False: 0}

        if self.node_type == 'bool2':
            symbol_type = 'int'
            if self.label == '==':
                self.label = dic[c0 == c1]
            elif self.label == '!=':
                self.label = dic[c0 != c1]
            elif self.label == '<':
                self.label = dic[c0 < c1]
            elif self.label == '<=':
                self.label = dic[c0 <= c1]
            elif self.label == '>':
                self.label = dic[c0 > c1]
            elif self.label == '>=':
                self.label = dic[c0 >= c1]

        if self.label == '&&':
            symbol_type = 'int'
            self.label = dic[bool(c0 and c1)]

        elif self.label == '||':
            symbol_type = 'int'
            self.label = dic[bool(c0 or c1)]

        # INTEGER OPERATION
        if '.' not in str(self.children[0].label) and '.' not in str(self.children[1].label):
            self.label = int(self.label)

        self.children = []
        self.node_type = 'rvalue'
        self.symbol_type = symbol_type
        return True

    def render_dot(self, graph=None):
        if graph is None:
            graph = Digraph(format='png')
        graph.node(str(self.id), str(self.label) + "\n(" + str(self.symbol_type) + ')')

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


class ASTVisitor:
    def __init__(self, node):
        self.startnode = node

    def clean_tree(self):
        queue = [self.startnode]
        # Get leaf nodes
        while len(queue) > 0:
            current_node = queue[0]

            queue = queue[1:]
            queue += current_node.children

            if len(current_node.children) == 1 and current_node.parent is not None and not 'for' in current_node.node_type \
                    and not 'condition' in current_node.node_type and not "case" in current_node.node_type \
                    and not 'return' in current_node.node_type and not 'args' in current_node.node_type:
                index = current_node.parent.children.index(current_node)
                current_node.parent.children.remove(current_node)
                current_node.parent.children[index:index] = current_node.children
                current_node.children[0].parent = current_node.parent
                del current_node

    def unary_fold(self):
        queue = [self.startnode]
        visited = []
        while len(queue) > 0:
            current_node = queue[0]
            queue = queue[1:]
            if current_node.id in visited:
                continue
            visited.append(current_node.id)

            if current_node.node_type in ['unary min', 'unary plus']:
                unary_list = [current_node]
                u_current_node = unary_list[0]
                while len(u_current_node.children) > 0:
                    u_current_node = unary_list[0]
                    visited.append(u_current_node.id)
                    if len(u_current_node.children) < 1:
                        unary_list = unary_list[1:]
                        break
                    unary_list.insert(0, u_current_node.children[1])

                for u_node in unary_list:
                    if not u_node.children[1].is_literal():
                        break
                    if u_node.node_type == 'unary min':
                        # print('-', u_node)
                        u_node.node_type = u_node.children[1].node_type
                        u_node.symbol_type = u_node.children[1].symbol_type
                        if u_node.node_type == 'float':
                            u_node.label = str(-float(u_node.children[1].label))
                        else:
                            u_node.label = str(-int(u_node.children[1].label))
                        del u_node.children[1]
                        del u_node.children[0]
                        u_node.children = []
                    elif u_node.node_type == 'unary plus':
                        # print('+', u_node)
                        if not u_node.children[1].is_literal():
                            break
                        u_node.node_type = u_node.children[1].node_type
                        u_node.symbol_type = u_node.children[1].symbol_type
                        u_node.label = u_node.children[1].label
                        del u_node.children[1]
                        del u_node.children[0]
                        u_node.children = []
                    else:
                        raise Exception('wtf gast')
            else:
                queue += current_node.children

    def maal(self):
        queue = [self.startnode]
        visited = []
        while len(queue) > 0:
            current_node = queue[0]
            queue = queue[1:]
            if current_node.id in visited:
                continue
            visited.append(current_node.id)
            queue += current_node.children
            if current_node.node_type == 'vm' or current_node.node_type == 'plus' or current_node.node_type == 'bool1':
                i = 0
                while i < len(current_node.children):
                    child = current_node.children[i]
                    if child.node_type in ["+", "-", "*", "/", "&&", "||", "boolop"]:
                        if i == 0:
                            if child.node_type == "+":
                                current_node.children.remove(child)
                                del child
                                continue
                            elif child.node_type == '-':
                                current_node.children[1].label = "-" + current_node.children[1].label
                                current_node.children.remove(child)
                                del child
                                continue
                            else:
                                raise Exception("very suspicious " + child.node_type)
                        try:
                            index = current_node.children.index(child)
                            current_node.children[index - 1].parent = child
                            current_node.children[index + 1].parent = child
                            child.children = [current_node.children[index - 1], current_node.children[index + 1]]
                            current_node.children.remove(current_node.children[index + 1])
                            current_node.children.remove(current_node.children[index - 1])
                        except:
                            print("halp")
                    else:
                        i += 1

                current_node.children[0].parent = current_node.parent
                index = current_node.parent.children.index(current_node)
                current_node.parent.children[index] = current_node.children[0]
                del current_node

    def fold_not(self):
        queue = [self.startnode]
        visited = []
        while len(queue) > 0:
            current_node = queue[len(queue) - 1]
            queue = queue[:-1]
            if current_node.id in visited:
                continue
            visited.append(current_node.id)

            queue = current_node.children + queue
            if current_node.node_type == 'Bool2':
                if len(current_node.children) != 0 and current_node.children[0].node_type == '!':

                    node_type = current_node.children[1].node_type
                    if node_type == '==':
                        node_type = '!='
                    elif node_type == '!=':
                        node_type = '=='
                    elif node_type == '>':
                        node_type = '<='
                    elif node_type == '<':
                        node_type = '>='
                    elif node_type == '<=':
                        node_type = '>'
                    elif node_type == '>=':
                        node_type = '<'

                    current_node.children[1].node_type = node_type

                    current_node.children.pop(0)

    def constant_folding(self):
        nodes = [self.startnode]
        while len(nodes) > 0:
            current_node = nodes[0]
            nodes = nodes[1:]

            if current_node.node_type in ["+", "-", "*", "/", "==", "!=", '>', '<', '>=', '<=', '&&', '||', 'boolop',
                                          'bool2']:
                current_node.only_literal_children()
            else:
                nodes += current_node.children
