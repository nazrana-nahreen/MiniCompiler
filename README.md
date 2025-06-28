For University Course Compiler Lab
# 🛠️ MiniCompiler

A simple compiler for a custom C-like language, built using Python and PLY (Python Lex-Yacc). This compiler can parse and execute a subset of programming constructs including variables, expressions, conditions, loops, and print statements.

---

## 📌 Features

- ✅ Arithmetic operations: `+`, `-`, `*`, `/`
- ✅ Logical operators: `and`, `or`, `not`
- ✅ Conditional execution: `if`, `else`
- ✅ Loops: `for`, `while`
- ✅ Print output: `print`
- ✅ Variable assignments and expressions
- ✅ Single-line comments with `//`

---

## 📁 Project Structure
MiniCompiler/
├── lexer.py # Lexical analyzer using PLY
├── parser.py # Parser + AST builder using PLY Yacc
├── interpreter.py # AST definitions and interpreter logic
├── main.py # Entry point for compiler
├── test_code.txt # Sample input code to run
├── requirements.txt # PLY dependency


---

## 🧠 How It Works

1. **Lexer**: Converts code into tokens
2. **Parser**: Builds an Abstract Syntax Tree (AST)
3. **Interpreter**: Walks the AST and executes the code

---

## 🖥️ Demo Code

Example code (`test_code.txt`):
```c
x = 5;
y = 10;
if x < y {
    print x + y;
} else {
    print x - y;
}

while x < 8 {
    print x;
    x = x + 1;
}

15
5
6
7

---

## 🧰 Used Tools & Technologies

| Tool / Library     | Purpose                              |
|--------------------|--------------------------------------|
| **Python 3.x**     | Core programming language            |
| **PLY (Lex & Yacc)** | Lexical analysis and parsing        |
| **PyCharm IDE**    | Development and debugging environment |
| **Markdown**       | Project documentation (`README.md`)  |
| **Git & GitHub**   | Version control and project sharing  |

---

## 👩‍💻 Developer

**Nazrana**  
Final Year Computer Science & Engineering Student  
🔬 Passionate about AI, compiler design, and building practical tools that help others learn.  
🛠️ Built this project solo to deeply understand the inner workings of how compilers and interpreters process code.

