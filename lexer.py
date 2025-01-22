import re

def lex(characters, TOKEN_SPECIFICATION):
    """ Tokenize the input string """
    pos = 0
    tokens = []
    for mo in re.finditer(r'|'.join('(?P<%s>%s)' % pair for pair in TOKEN_SPECIFICATION), characters):
        kind = mo.lastgroup
        value = mo.group()
        if kind == 'NEWLINE':
            pos += 1
            continue
        elif kind == 'SKIP':
            continue
        elif kind == 'MISMATCH':
            raise RuntimeError(f'{value!r} unexpected on line {pos}')
        tokens.append((kind, value))
    return tokens
