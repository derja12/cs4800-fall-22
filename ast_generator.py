#!/usr/bin/python3
import ast
import astpretty

if __name__ == "__main__":
    fin = open(input("filename? "), "r")
    fileContent = ""
    for line in fin:
        fileContent += line
    node = ast.parse(fileContent)
    fin.close()
    astpretty.pprint(node)
    print(ast.dump(node))