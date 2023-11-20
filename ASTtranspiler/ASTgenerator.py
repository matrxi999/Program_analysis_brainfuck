class Node:
    def __init__(self, kind, value=None):
        self.kind = kind
        self.value = value
        self.children = []

    def add_child(self, child):
        self.children.append(child)

class BrainfuckParser:
    def __init__(self, code):
        self.code = code
        self.position = 0

    def parse(self):
        root = Node("root")
        root.children = self._parse_nodes()
        return root

    def _parse_nodes(self):
        nodes = []
        while self.position < len(self.code):
            char = self.code[self.position]
            if char in "><+-.,":  # Basic commands
                nodes.append(Node("command", char))
                self.position += 1
            elif char == '[':  # Start of loop
                self.position += 1
                loop_node = Node("loop_start")
                loop_body = self._parse_nodes()
                for node in loop_body:
                    loop_node.add_child(node)
                nodes.append(loop_node)
            elif char == ']':  # End of loop
                self.position += 1
                end_loop_node = Node("loop_end")
                nodes.append(end_loop_node)
                return nodes
            else:
                self.position += 1  # Ignore non-command characters
        return nodes

def print_ast(node, indent=0):
    print("  " * indent + node.kind, node.value if node.value else "")
    for child in node.children:
        print_ast(child, indent + 1)

# Example usage
code = """>    
                               + +    
                              +   +    
                             [ < + +    
                            +       +    
                           + +     + +    
                          >   -   ]   >    
                         + + + + + + + +    
                        [               >    
                       + +             + +    
                      <   -           ]   >    
                     > + + >         > > + >    
                    >       >       +       <    
                   < <     < <     < <     < <    
                  <   [   -   [   -   >   +   <    
                 ] > [ - < + > > > . < < ] > > >    
                [                               [    
               - >                             + +    
              +   +                           +   +    
             + + [ >                         + + + +    
            <       -                       ]       >    
           . <     < [                     - >     + <    
          ]   +   >   [                   -   >   +   +    
         + + + + + + + +                 < < + > ] > . [    
        -               ]               >               ]    
       ] +             < <             < [             - [    
      -   >           +   <           ]   +           >   [    
     - < + >         > > - [         - > + <         ] + + >    
    [       -       <       -       >       ]       <       <    
   < ]     < <     < <     ] +     + +     + +     + +     + +    
  +   .   +   +   +   .   [   -   ]   <   ]   +   +   +   +   +  """
parser = BrainfuckParser(code)
ast = parser.parse()
print_ast(ast)

print("")
print("BF code: " + code)


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

# Generate DOT output
dot_output = generate_dot(ast)
with open("Program_analysis_brainfuck\ASTtranspiler\generatedFiles\ASTgraph.dot", "w", encoding="utf-8") as text_file:
    text_file.write(dot_output)