import ply.yacc as yacc
from lexer import tokens
from interpreter import (
    Program, StatementList, Assignment, Print,
    IfElse, ForLoop, WhileLoop, BinOp, UnOp, Number, Var
)

def p_program(p):
    """program : statement_list"""
    p[0] = Program(p[1])

def p_statement_list(p):
    """statement_list : statement_list statement
                      | statement"""
    if len(p) == 3:
        p[0] = p[1] + [p[2]]
    else:
        p[0] = [p[1]]

def p_statement(p):
    """statement : assignment
                 | if_statement
                 | for_loop
                 | while_loop
                 | print_statement"""
    p[0] = p[1]

def p_assignment(p):
    "assignment : ID ASSIGN expression SEMI"
    p[0] = Assignment(p[1], p[3])

def p_print_statement(p):
    "print_statement : PRINT expression SEMI"
    p[0] = Print(p[2])

def p_if_statement(p):
    """if_statement : IF expression LBRACE statement_list RBRACE
                    | IF expression LBRACE statement_list RBRACE ELSE LBRACE statement_list RBRACE"""
    if len(p) == 6:
        p[0] = IfElse(p[2], StatementList(p[4]))
    else:
        p[0] = IfElse(p[2], StatementList(p[4]), StatementList(p[8]))

def p_for_loop(p):
    """for_loop : FOR ID ASSIGN expression SEMI expression SEMI ID ASSIGN expression LBRACE statement_list RBRACE"""
    p[0] = ForLoop(
        var_name=p[2],
        start_expr=p[4],
        cond_expr=p[6],
        step_var=p[8],
        step_expr=p[10],
        body=StatementList(p[12])
    )

def p_while_loop(p):
    """while_loop : WHILE expression LBRACE statement_list RBRACE"""
    p[0] = WhileLoop(p[2], StatementList(p[4]))

def p_expression_binop(p):
    """expression : expression PLUS expression
                  | expression MINUS expression
                  | expression MUL expression
                  | expression DIV expression
                  | expression LT expression
                  | expression GT expression
                  | expression LE expression
                  | expression GE expression
                  | expression EE expression
                  | expression NE expression
                  | expression AND expression
                  | expression OR expression"""
    p[0] = BinOp(p[1], p[2], p[3])

def p_expression_not(p):
    "expression : NOT expression"
    p[0] = UnOp('not', p[2])

def p_expression_group(p):
    "expression : LPAREN expression RPAREN"
    p[0] = p[2]

def p_expression_number(p):
    "expression : NUMBER"
    p[0] = Number(p[1])

def p_expression_id(p):
    "expression : ID"
    p[0] = Var(p[1])

def p_error(p):
    if p:
        print(f"Syntax error at token {p.type}({p.value})")
    else:
        print("Syntax error at EOF")

parser = yacc.yacc()
