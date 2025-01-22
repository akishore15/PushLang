import re

# Token specification
TOKEN_SPECIFICATION = [
    ('MULTILINE_COMMENT', r'/\*.*?\*/', re.S),
    ('COMMENT', r'//.*'),
    ('PRINT', r'cout

\[\]

'),
    ('READ', r'readcout

\[\]

'),
    ('EXPONENT', r'\*\*'),
    ('MULTIPLY', r'\*'),
    ('DIVISION', r'/'),
    ('MODULO', r'%'),
    ('ADD', r'\+'),
    ('SUBTRACT', r'-'),
    ('LIST', r'\{.*?\}', re.S),
    ('CLASS', r'class'),
    ('FUNCTION', r'func'),
    ('FOR_LOOP', r'for:[^;]+;'),
    ('WHILE_LOOP', r'while:[^;]+;'),
    ('IFELSE', r'ifelse\s*\(.*?\)\s*\{.*?\}\s*\{.*?\}'),
    ('ELSEIF', r'elseif\s*\(.*?\)\s*\{.*?\}'),
    ('DIVISION_SECTION', r'division\s*[^\n]+'),
    ('VARIABLE', r'\$\w+'),
    ('INTEGER', r'\d+'),
    ('IDENTIFIER', r'\w+'),
    ('NEWLINE', r'\n'),
    ('SKIP', r'[ \t]+'),
    ('MISMATCH', r'.')
]
