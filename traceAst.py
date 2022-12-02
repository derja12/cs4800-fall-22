#does not work with python 2 so make sure on that one
import ast
import astpretty
# import traceAst
from unit_tests import *
import trace
import sys

def test():
    var = 10 + 10
    stringVar = "Hello,"
    stringVar2 = " World!"

    return stringVar + stringVar2 + str(var)

# file = open("all_sorts.py")
# tree = ast.parse("all_sorts.py", mode='eval')
# print(ast.dump(tree))
# print(ast.parse(open("all_sorts.py")))


fin = open("all_sorts.py", "r")
fileContent = ""
for line in fin:
    fileContent += line
node = ast.parse(fileContent)
fin.close()

# astpretty.pprint(node)
# print(ast.dump(node))
tracer = trace.Trace(
    ignoredirs=[sys.prefix, sys.exec_prefix],
    trace=0,
    count=1
)
tracer.run("main_testing('TestMergeSort.test_1_expected_use')")
r = tracer.results()
r.write_results(show_missing=True, coverdir=".")
# traceAst

