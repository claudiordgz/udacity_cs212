from json_parser import grammar, parse

REGRAMMAR = grammar("""RE => ## Description
""", whitespace='')

def parse_re(pattern):
    return convert(parse('RE', pattern, REGRAMMAR))

def convert(tree):
    #more code