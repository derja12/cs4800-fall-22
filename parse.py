import astor
import ast
import all_sorts
import inspect
import astpretty

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

#will edit the return value
def editReturn(node, edit):
    if isinstance(node, ast.Return):
        newNode = node
        newNode.value = ast.parse(edit)
        node = newNode

def main():
    bs = inspect.getsource(all_sorts.Bubble)
    bubbleAST = functionToAST(bs)
    
    walker = ast.walk(bubbleAST)

    
    for node in walker:
        if isinstance(node, ast.Return):
            newNode = node
            newNode.value = ast.parse("YESYESYES")
            # newNode.kind = ast.Bo
            node = newNode

            # astpretty.pprint(node)
            # return
            # node = ast.If(left= True, body= node.body)
            
    # print(bubbleAST)
    astpretty.pprint(bubbleAST)
    # print(astToSource(bubbleAST))
    


if __name__ == "__main__":
    main()
    # import ast
    # class StringWrapper(ast.NodeTransformer):
    #     """Wraps all strings in 'START ' + string + ' END'. """
    #     def visit_Str(self, node):
    #         return ast.Call(func=ast.Name(id='wrap_string', ctx=ast.Load()),
    #                         args=[node], keywords=[])

    # def wrap_string(s):
    #     return 'START ' + s + ' END'

    # code = "print('test string')"
    # print(code)
    # print()

    # print("Without AST transformation:")
    # exec(code)
    # print()

    # print("With AST transformation:")
    # tree = ast.parse(code)
    # tree = StringWrapper().visit(tree)

    # # Add lineno & col_offset to the nodes we created
    # ast.fix_missing_locations(tree)
    # co = compile(tree, "<ast>", "exec")
    # exec(co)


    
        # left=Subscript(
        #     lineno=10,
        #     col_offset=15,
        #     end_lineno=10,
        #     end_col_offset=19,
        #     value=Name(lineno=10, col_offset=15, end_lineno=10, end_col_offset=16, id='L', ctx=Load()),
        #     slice=Name(lineno=10, col_offset=17, end_lineno=10, end_col_offset=18, id='i', ctx=Load()),
        #     ctx=Load(),
        # ),
        # ops=[Gt()],
        # comparators=[
        #     Subscript(
                
        #         value=Name(lineno=10, col_offset=22, end_lineno=10, end_col_offset=23, id='L', ctx=Load()),
        #         slice=BinOp(
                
        #             left=Name(lineno=10, col_offset=24, end_lineno=10, end_col_offset=25, id='i', ctx=Load()),
        #             op=Add(),
        #             right=Constant(lineno=10, col_offset=26, end_lineno=10, end_col_offset=27, value=1, kind=None),
        #         ),
        #         ctx=Load(),
        #     ),
        # ],