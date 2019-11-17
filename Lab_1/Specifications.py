special = ['identifier', 'constant']

operators = ['+', '-', '*', '/',
             '<=', '>=', '>', '<', '==', '!=',
             '=',
             '>>', '<<',
             '&&', '||',
             '++', '--']

reserved = ['int', 'char', 'cin', 'cout', 'for', 'do', 'string',
            'if', 'else', 'while', 'return', 'array', 'main']

separators = ['[', ']', '{', '}', '(', ')', ';', ' ', ',']

codification = special + reserved + operators + separators
codification_table = dict([(codification[i], i) for i in range(len(codification))])
