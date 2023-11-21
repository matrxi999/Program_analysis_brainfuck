from graphviz import Source
import os

# Script to visualise optimized AST

os.environ["PATH"] += os.pathsep + 'C:/Program Files/Graphviz/bin/'

with open("ASTtranspiler/generatedFiles/ASTgraphOptimized.dot", 'r') as file:
    astOpt_dot_code = file.read()

s = Source(astOpt_dot_code, filename="ASTtranspiler/generatedFiles/ASTgraphOptimized", format="png")
s.view()