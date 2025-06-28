from parser import parser
from interpreter import exec_stmt

print("MiniCompiler Ready. Type 'exit' to quit.\n")

try:
    with open("test_code.txt") as f:
        code = f.read()
        ast = parser.parse(code)
        exec_stmt(ast)
except FileNotFoundError:
    pass

while True:
    try:
        line = input(">> ")
    except EOFError:
        break
    if line.strip() == "exit":
        break
    ast = parser.parse(line)
    exec_stmt(ast)
