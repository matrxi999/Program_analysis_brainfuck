from graphviz import Source
import os

os.environ["PATH"] += os.pathsep + 'C:/Program Files/Graphviz/bin/'

with open("generatedFiles/ASTtranspiler/ASTgraphOptimized.dot", 'r') as file:
    astOpt_dot_code = file.read()

s = Source(astOpt_dot_code, filename="generatedFiles/ASTtranspiler/ASTgraphOptimized", format="png")
s.view()