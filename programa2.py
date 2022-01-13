# -*- coding: utf-8 -*-

import sys
import io
import nltk

def parse(s):
    grammar = """
    S -> A | R | M | D | P | E | N | V | B | X 
    A -> S ' ' '+' ' ' S
    R -> S ' ' '-' ' ' S
    M -> S ' ' '*' ' ' S
    D -> S ' ' '/' ' ' S
    A -> S '^' S
    E -> '-' S
    N -> N '1' | N '2' | N '3' | N '4' | N '5' | N '6' | N '7' | N '8' | N '9' | N '0' | '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9' | '0' 
    V -> '|' S '|'
    B -> '(' S ')'
    X -> N '.' N | '.' N 
    """
    grammar = nltk.CFG.fromstring(grammar)
    s_tokenized = list(s.strip())
    parser = nltk.LeftCornerChartParser(grammar)
    tree = list(parser.parse(s_tokenized))[:1]
    return tree

if __name__ == '__main__':
    archivo_entrada = sys.argv[1]
    archivo_salida = sys.argv[2]
    f = io.open(archivo_entrada, 'r', newline='\n', encoding='utf-8')
    s = f.read()
    f.close()
    try:
      tree = parse(s)
      if tree:
          salida = "PERTENECE"
      else:
          salida = "NO PERTENECE"
    except ValueError:
      salida = "NO CUBRE"
    f = io.open(archivo_salida, 'w', newline='\n', encoding='utf-8')
    f.write(salida)
    f.close()