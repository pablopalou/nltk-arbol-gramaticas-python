# -*- coding: utf-8 -*-

import sys
import io
import nltk
from nltk import Tree

def parse(s):
    grammar = """
    S -> '(' X ' ' S ' ' S ')' | '(' ')'
    X -> '-' N | N
    N -> N '1' | N '2' | N '3' | N '4' | N '5' | N '6' | N '7' | N '8' | N '9' | N '0' | '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9' | '0'  
    """
    grammar = nltk.CFG.fromstring(grammar)
    s_tokenized = list(s.strip())
    parser = nltk.LeftCornerChartParser(grammar)
    tree = list(parser.parse(s_tokenized))[:1]
    return tree

def darVuelta(tree):
  if len(tree) != 7:
    return tree
  else:
    tree[3] = darVuelta(tree[3])
    tree[5] = darVuelta(tree[5])
    if len(tree[1]) == 2:
      temp = tree[3]
      tree[3] = tree[5]
      tree[5] = temp
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
          tree = darVuelta(tree[0])
          salida = ""
          for hoja in tree.leaves():
            salida += hoja
      else:
          salida = "NO PERTENECE"
    except ValueError:
      salida = "NO CUBRE"
    f = io.open(archivo_salida, 'w', newline='\n', encoding='utf-8')
    f.write(salida)
    f.close()