import sys
import io
import nltk

def parse(s):
    grammar = """
    S -> '1' B | '2' C | '3' A 
    A -> '1' D | '2' E | '3' S 
    B -> '1' S | '2' G | '3' D 
    C -> '1' G | '2' S | '3' E 
    D -> '1' A | '2' F | '3' B | '1'
    E -> '1' F | '2' A | '3' C 
    F -> '1' E | '2' D | '3' G 
    G -> '1' C | '2' B | '3' F 
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