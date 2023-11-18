from graphviz import Source
import os

os.environ["PATH"] += os.pathsep + 'C:/Program Files/Graphviz/bin/'

with open("ASTtranspiler/ASTgraph.dot", 'r') as file:
    ast_dot_code = file.read()

s = Source(ast_dot_code, filename="ASTtranspiler/ASTgraph", format="png")
s.view()