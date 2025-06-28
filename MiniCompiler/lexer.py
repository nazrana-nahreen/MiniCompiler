import ply.lex as lex

# Reserved words
reserved = {
    'if': 'IF',
    'else': 'ELSE',
    'for': 'FOR',
    'while': 'WHILE',
    'print': 'PRINT',
    'and': 'AND',
    'or': 'OR',
    'not': 'NOT'
}

# Token list
tokens = [
    'ID', 'NUMBER',
    'PLUS', 'MINUS', 'MUL', 'DIV',
    'ASSIGN',
    'LT', 'GT', 'LE', 'GE', 'EE', 'NE',
    'LPAREN', 'RPAREN',
    'LBRACE', 'RBRACE',
    'SEMI'
] + list(reserved.values())

# Token regex definitions
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_MUL     = r'\*'
t_DIV     = r'/'
t_ASSIGN  = r'='
t_LT      = r'<'
t_GT      = r'>'
t_LE      = r'<='
t_GE      = r'>='
t_EE      = r'=='
t_NE      = r'!='
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_LBRACE  = r'\{'
t_RBRACE  = r'\}'
t_SEMI    = r';'

# Ignore spaces and tabs
t_ignore = ' \t'

# Handle newlines
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Handle numbers
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Handle identifiers (variables and reserved keywords)
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'ID')
    return t

# Handle single-line comments (// ...)
def t_COMMENT(t):
    r'//.*'
    pass  # Just skip them

# Error handler
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()
