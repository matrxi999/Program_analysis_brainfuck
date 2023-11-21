from graphviz import Source
import os

# Script to visualise unoptimized AST

os.environ["PATH"] += os.pathsep + 'C:/Program Files/Graphviz/bin/'

with open("ASTtranspiler/generatedFiles/ASTgraph.dot", 'r') as file:
    ast_dot_code = file.read()

s = Source(ast_dot_code, filename="ASTtranspiler/generatedFiles/ASTgraph", format="png")
s.view()