# Takes optimized python code and makes AST to visualize it later

class Node:
    def __init__(self, kind, value=None):
        self.kind = kind
        self.value = value
        self.children = []

    def add_child(self, child):
        self.children.append(child)

class PythonParser:
    def __init__(self, code):
        self.code = code.split('\n')
        self.position = 0

    def parse(self):
        root = Node("root")
        root.children = self._parse_nodes()
        return root

    def _parse_nodes(self):
        nodes = []
        while self.position < len(self.code):
            line = self.code[self.position].strip()
            if line.startswith("add(") or line.startswith("subtract("):
                nodes.append(Node("command", line))
            elif line.startswith("data[") or line.startswith("index"):
                nodes.append(Node("assignment", line))
            elif line.startswith("while"):
                loop_node = Node("loop_start")
                self.position += 1
                loop_body = self._parse_nodes()
                for node in loop_body:
                    loop_node.add_child(node)
                nodes.append(loop_node)
            elif line.startswith("# End of loop"):
                nodes.append(Node("loop_end"))
                return nodes
            elif line.startswith("output()"):
                nodes.append(Node("command", "output()"))
            self.position += 1
        return nodes

def print_ast(node, indent=0):
    print("  " * indent + node.kind, node.value if node.value else "")
    for child in node.children:
        print_ast(child, indent + 1)

def to_dot(node, dot_string='', parent_id=0, current_id=[1]):
    """Converts the AST to DOT format for Graphviz."""
    node_id = current_id[0]
    current_id[0] += 1

    label = node.kind + (": " + node.value if node.value else "")
    dot_string += f'  node{node_id} [label="{label}"];\n'
    if node_id != 1:  # Don't draw edge for root
        dot_string += f'  node{parent_id} -> node{node_id};\n'

    for child in node.children:
        dot_string = to_dot(child, dot_string, node_id, current_id)

    return dot_string

def generate_dot(ast):
    dot_header = "digraph AST {\n  node [shape=box];\n"
    dot_footer = "}\n"
    return dot_header + to_dot(ast) + dot_footer

# Example usage
python_code = """
add(2)
while data[index] != 0:
    add(1)
    temp = data[index]
    data[index] = 0
    data[index + 1] = temp
    # End of loop
subtract(2)
"""

parser = PythonParser(python_code)
ast = parser.parse()
print_ast(ast)

# Generate DOT output
dot_output = generate_dot(ast)
with open("ASTtranspiler/generatedFiles/ASTgraphOptimized.dot", "w", encoding="utf-8") as text_file:
    text_file.write(dot_output)