import astor
import ast

# This file has helper methods for 
def functionToAST(code):
    return ast.parse(code)

def astToSource(ast):
    return astor.to_source(ast)

def astToFile(ast, filename):
    file = open(filename, "w")
    file.write(astor.to_source(ast))
    file.close()

def fileToAst(filename):
    file = open(filename, "r")
    code = ""
    for line in file:
        code += line
    return ast.parse(code)

