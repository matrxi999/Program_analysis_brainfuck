import graphviz

def generate_graphviz_from_brainfuck(code):
    dot = graphviz.Digraph(engine='dot')  # Use the dot layout engine
    current_y = 0
    current_x = 0
    node_count = 0
    loop_stack = []
    dot.node(str(node_count), label="Start", pos=f"{current_x},{current_y}!")
    node_count += 1

    for char in code:
        if char == '+':
            current_y -= 1
            dot.node(str(node_count), label="+", pos=f"{current_x},{current_y}!")
            dot.edge(str(node_count - 1), str(node_count))
            node_count += 1
        elif char == '-':
            current_y -= 1
            dot.node(str(node_count), label="-", pos=f"{current_x},{current_y}!")
            dot.edge(str(node_count - 1), str(node_count))
            node_count += 1
        elif char == '.':
            current_y -= 1
            dot.node(str(node_count), label="Out", pos=f"{current_x},{current_y}!")
            dot.edge(str(node_count - 1), str(node_count))
            node_count += 1
        elif char == '>':
            current_x += 1
            current_y -= 1
            dot.node(str(node_count), label=">", pos=f"{current_x},{current_y}!")
            dot.edge(str(node_count - 1), str(node_count))
            node_count += 1
        elif char == '<':
            current_x -= 1
            current_y -= 1
            dot.node(str(node_count), label="<", pos=f"{current_x},{current_y}!")
            dot.edge(str(node_count - 1), str(node_count))
            node_count += 1
        elif char == '[':
            dot.node(str(node_count), label="[", pos=f"{current_x},{current_y}!")
            dot.edge(str(node_count - 1), str(node_count))
            loop_stack.append((node_count - 1, current_x))
            node_count += 1
            current_y -= 1
        elif char == ']':
            start_node, start_x = loop_stack.pop()
            dot.node(str(node_count), label="]", pos=f"{current_x},{current_y}!")
            dot.edge(str(node_count - 1), str(node_count))
            dot.edge(str(node_count), str(start_node))
            node_count += 1
            current_y -= 1
            current_x = start_x

    dot.node(str(node_count), label="End", pos=f"{current_x},{current_y}!")
    dot.edge(str(node_count - 1), str(node_count))

    return dot


if __name__ == '__main__':
    brainfuck_code = "++[++.<+>.]+>"
    graph = generate_graphviz_from_brainfuck(brainfuck_code)
    graph.render('brainfuck_graph', format='png', cleanup=True)
