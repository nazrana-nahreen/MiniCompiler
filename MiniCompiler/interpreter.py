from symbols import variables

class ASTNode:
    pass

class Program(ASTNode):
    def __init__(self, statements):
        self.statements = statements

class StatementList(ASTNode):
    def __init__(self, statements):
        self.statements = statements

class Assignment(ASTNode):
    def __init__(self, var_name, expr):
        self.var_name = var_name
        self.expr = expr

class Print(ASTNode):
    def __init__(self, expr):
        self.expr = expr

class IfElse(ASTNode):
    def __init__(self, condition, if_body, else_body=None):
        self.condition = condition
        self.if_body = if_body
        self.else_body = else_body

class ForLoop(ASTNode):
    def __init__(self, var_name, start_expr, cond_expr, step_var, step_expr, body):
        self.var_name = var_name
        self.start_expr = start_expr
        self.cond_expr = cond_expr
        self.step_var = step_var
        self.step_expr = step_expr
        self.body = body

class WhileLoop(ASTNode):
    def __init__(self, condition, body):
        self.condition = condition
        self.body = body

class BinOp(ASTNode):
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

class UnOp(ASTNode):
    def __init__(self, op, expr):
        self.op = op
        self.expr = expr

class Number(ASTNode):
    def __init__(self, value):
        self.value = value

class Var(ASTNode):
    def __init__(self, name):
        self.name = name

# Interpreter walks AST:

def eval_expr(node):
    if isinstance(node, Number):
        return node.value
    elif isinstance(node, Var):
        return variables.get(node.name, 0)
    elif isinstance(node, BinOp):
        left = eval_expr(node.left)
        right = eval_expr(node.right)
        if node.op == '+': return left + right
        if node.op == '-': return left - right
        if node.op == '*': return left * right
        if node.op == '/': return left / right
        if node.op == '<': return left < right
        if node.op == '>': return left > right
        if node.op == '<=': return left <= right
        if node.op == '>=': return left >= right
        if node.op == '==': return left == right
        if node.op == '!=': return left != right
        if node.op == 'and': return left and right
        if node.op == 'or': return left or right
    elif isinstance(node, UnOp):
        val = eval_expr(node.expr)
        if node.op == 'not': return not val
    else:
        raise Exception(f"Unknown expression node: {node}")

def exec_stmt(node):
    if isinstance(node, Program):
        for stmt in node.statements:
            exec_stmt(stmt)
    elif isinstance(node, StatementList):
        for stmt in node.statements:
            exec_stmt(stmt)
    elif isinstance(node, Assignment):
        val = eval_expr(node.expr)
        variables[node.var_name] = val
    elif isinstance(node, Print):
        val = eval_expr(node.expr)
        print(val)
    elif isinstance(node, IfElse):
        cond = eval_expr(node.condition)
        if cond:
            exec_stmt(node.if_body)
        elif node.else_body is not None:
            exec_stmt(node.else_body)
    elif isinstance(node, ForLoop):
        variables[node.var_name] = eval_expr(node.start_expr)
        while eval_expr(node.cond_expr):
            exec_stmt(node.body)
            variables[node.step_var] = eval_expr(node.step_expr)
    elif isinstance(node, WhileLoop):
        while eval_expr(node.condition):
            exec_stmt(node.body)
    else:
        raise Exception(f"Unknown statement node: {node}")
