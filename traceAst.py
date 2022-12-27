#does not work with python 2 so make sure on that one
import ast
import marshal
import pickle
import astpretty
# import traceAst
import trace
import sys
import astor
import parse

def test():
    var = 10 + 10
    stringVar = "Hello,"
    stringVar2 = " World!"

    return stringVar + stringVar2 + str(var)

# file = open("all_sorts.py")
# tree = ast.parse("all_sorts.py", mode='eval')
# print(ast.dump(tree))
# print(ast.parse(open("all_sorts.py")))


node = parse.fileToAst("all_sorts.py")
# print(astpretty.pprint(node))

parse.astToFile(node, "output2.py")

# astpretty.pprint(node)
# print(ast.dump(node))
tracer = trace.Trace(
    ignoredirs=[sys.prefix, sys.exec_prefix]
)

fileOutput = astor.to_source(node=node)



# trying to get writing to a file to work
file = open("output.py", "w") 
file.write(fileOutput)
# # marshal.dump(fileOutput.__str__, file)
file.close()

# tracing execution
# tracer.run(node)
# r = tracer.results()
# r.write_results(show_missing=True, coverdir=".")
# traceAst

