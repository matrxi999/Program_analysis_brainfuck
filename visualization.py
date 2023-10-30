import graphviz

def generate_graphviz_from_brainfuck(code):
    dot = graphviz.Digraph()

    dot.node("start", label="Start")
    dot.node("end", label="End")

    loop_stack = []
    current_node = "start"

    for idx, char in enumerate(code):
        if char == '+':
            dot.node(f"add_{idx}", label="+")
            dot.edge(current_node, f"add_{idx}")
            current_node = f"add_{idx}"
        elif char == '-':
            dot.node(f"subtract_{idx}", label="-")
            dot.edge(current_node, f"subtract_{idx}")
            current_node = f"subtract_{idx}"
        elif char == '.':
            dot.node(f"output_{idx}", label="Output")
            dot.edge(current_node, f"output_{idx}")
            current_node = f"output_{idx}"
        elif char == '>':
            dot.node(f"move_right_{idx}", label=">")
            dot.edge(current_node, f"move_right_{idx}")
            current_node = f"move_right_{idx}"
        elif char == '<':
            dot.node(f"move_left_{idx}", label="<")
            dot.edge(current_node, f"move_left_{idx}")
            current_node = f"move_left_{idx}"
        elif char == '[':
            dot.node(f"loop_start_{idx}", label="Loop Start")
            dot.edge(current_node, f"loop_start_{idx}")
            loop_stack.append((idx, f"loop_start_{idx}"))
            current_node = f"loop_start_{idx}"
        elif char == ']':
            start_idx, start_node = loop_stack.pop()
            dot.node(f"loop_end_{idx}", label="Loop End")
            dot.edge(current_node, f"loop_end_{idx}")
            dot.edge(f"loop_end_{idx}", start_node)
            current_node = f"loop_end_{idx}"

    dot.edge(current_node, "end")
    return dot


if __name__ == '__main__':
    brainfuck_code = "++++++++++[>+++++++>++++[++++++>+++>]+<<<<-]>++.>+.+++++++..+++.>++.<<+++++++++++++++.>.+++.------.--------.>+.>."
    graph = generate_graphviz_from_brainfuck(brainfuck_code)
    graph.render('brainfuck_graph', format='png', cleanup=True)
