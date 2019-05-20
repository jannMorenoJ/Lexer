import ply3.ply.lex as lex
import re
import codecs
import os
import sys

reservadas = ['and', 'constantes', 'hasta', 'matriz', 'paso', 'regitro', 'sino', 'vector', 'archivo', 'desde', 'inicio', 'mientras', 'subrutina', 'repetir', 'tipos', 'caso', 'eval', 'lib', 'not', 'programa', 'retorna', 'var', 'const', 'fin', 'libext', 'or', 'ref', 'si', 'variables', 'numerico', 'imprimir', 'leer', 'dim',
              'cls', 'set_ifs', 'abs', 'arctan', 'ascii', 'cos', 'dec', 'eof', 'exp', 'get_ifs', 'inc', 'int', 'log', 'lower', 'mem', 'ord', 'paramval', 'pcount', 'pos', 'random', 'sec', 'set_stdin', 'set_stdout', 'sin', 'sqrt', 'srt', 'strdup', 'strlen', 'tan', 'upper', 'val', 'logico', 'verdadero', 'TRUE', 'FALSE', 'SI', 'NO']
operadores = ['tk_punto', 'tk_coma', 'tk_dospuntos', 'tk_par_izq', 'tk_par_der', 'tk_punto_y_coma', 'tk_asig', 'tk_llave_izq', 'tk_llave_der', 'tk_corchete_izq', 'tk_corchete_der', 'tk_distinto',
              'tk_igual_que', 'tk_menor_que', 'tk_mayor_que', 'tk_menor_igual_que', 'tk_mayor_igual_que', 'tk_potenciacion', 'tk_modulo', 'tk_division', 'tk_suma', 'tk_resta', 'tk_multiplicacion']
tokens = reservadas + operadores + ['id', 'tk_numero', 'tk_cadena']

'''
reservadas = {
  'and': 'and',
  'constantes' : 'constantes',
  'hasta' : 'hasta',
  'matriz' : 'matriz',
  'paso' : 'paso',
  'regitro' : 'regitro',
  'sino' : 'sino',
  'vector' : 'vector',
  'archivo' : 'archivo',
  'desde' : 'desde',
  'inicio' : 'inicio',
  'mientras' : 'mientras',
  'subrutina' :'subrutina',
  'repetir' : 'repetir',
  'tipos' : 'tipos',
  'caso' : 'caso',
  'eval' : 'eval',
  'lib' : 'lib',
  'not': 'not',
  'programa' : 'programa',
  'retorna' : 'retorna',
  'var' : 'var',
  'const' : 'const',
  'fin' : 'fin',
  'libext' : 'libext',
  'or' : 'or',
  'ref' : 'ref',
  'si' : 'si',
  'variables' : 'variables',
  'numerico' : 'numerico',
  'imprimir' : 'imprimir',
  'leer': 'leer',
  'dim' : 'dim',
  'cls' : 'cls',
  'set_ifs' : 'set_ifs',
  'abs' : 'abs',
  'arctan' : 'arctan',
  'ascii' : 'ascii',
  'cos' : 'cos',
  'dec' : 'dec',
  'eof' : 'eof',
  'exp' : 'exp',
  'get_ifs' : 'get_ifs',
  'inc' : 'inc',
  'int' : 'int',
  'log' : 'log',
  'lower' : 'lower',
  'mem' : 'mem',
  'ord' : 'ord',
  'paramval' : 'paramval',
  'pcount' : 'pcount',
  'pos' : 'pos',
  'random' : 'random',
  'sec' : 'sec',
  'set_stdin' : 'set_stdin',
  'set_stdout' : 'set_stdout',
  'sin' : 'sin',
  'sqrt' : 'sqrt',
  'srt' : 'srt',
  'strdup' : 'strdup',
  'strlen' : 'strlen',
  'tan' : 'tan',
  'upper' : 'upper',
  'val' : 'val',
  'logico' : 'logico',
  'verdadero' : 'verdadero'
}

tokens = tokens + list(reservadas.values())
'''


def find_column(input, token):
    line_start = input.rfind('\n', 0, token.lexpos) + 1
    return (token.lexpos - line_start) + 1


def encontrar_columna(token):
    return find_column(cadena, token)


t_ignore = '\t'
t_tk_punto = r'\.'
t_tk_coma = r','
t_tk_dospuntos = r':'
t_tk_par_izq = r'\('
t_tk_par_der = r'\)'
t_tk_punto_y_coma = r';'
t_tk_asig = r'='
t_tk_llave_izq = r'\['
t_tk_llave_der = r'\]'
t_tk_corchete_izq = r'\{'
t_tk_corchete_der = r'\}'
t_tk_distinto = r'<>'
t_tk_igual_que = r'=='
t_tk_menor_que = r'<'
t_tk_mayor_que = r'>'
t_tk_menor_igual_que = r'<='
t_tk_mayor_igual_que = r'>='
t_tk_potenciacion = r'\^'
t_tk_modulo = r'%'
t_tk_division = r'\/'
t_tk_multiplicacion = r'\*'
t_tk_suma = r'\+'
t_tk_resta = r'\-'


def t_comment(t):
    r'(\/\*(.|\n)*?\*\/)|(\/\/.*)'
    t.lexer.lineno += t.value.count('\n')
    pass


def t_id(t):
    r'[a-zA-ZñÑ][\wñÑ]*'
    if(t.value in reservadas):
        t.type = t.value
    return t


def t_new_line(t):
    r'\n'
    t.lexer.lineno += len(t.value)


def t_space(t):
    r'\s'
    pass


def t_tk_numero(t):
    r'((\+|\-)?\d+(\.\d+)?((e|E)(\+|\-)\d+)?)'
    return t


def t_tk_cadena(t):
    r"(\'((\\\'|[^\'\n])*(\+\n)?)*\')|(\"((\\\"|[^\"\n])*(\+\n)?)*\")"
    return t


def t_error(t):
    t.lexpos = encontrar_columna(t)
    print('>>> Error lexico(linea:'+str(t.lineno)+',posicion:'+str(t.lexpos)+')')
    sys.exit()
    t.lexer.skip(1)


def buscar_fichero(directorio):
    ficheros = []
    numArchivo = ''
    respuesta = False
    cont = 1
    for base, dirs, files in os.walk(directorio):
        ficheros.append(files)
    print(ficheros[0][0])
    for file in files:
        print(str(cont)+" "+file)
        cont += 1
    while respuesta == False:
        numArchivo = input('\nNumero de la prueba: ')
        for file in files:
            if file == files[int(numArchivo)-1]:
                respuesta = True
                break
    return files[int(numArchivo)-1]


directorio = '/home/jann/Documents/UN/2019-1/Lenguajes/analizadorLexico/lex/documents/'
archivo = buscar_fichero(directorio)
test = directorio+archivo
fo = codecs.open(test, 'r', 'utf-8')
cadena = fo.read()
fo.close()

analizador = lex.lex()
analizador.input(cadena)

while True:
    tok = analizador.token()
    if not(tok):
        break
    tok.lexpos = encontrar_columna(tok)
    if((tok.type in reservadas)or(tok.type in operadores)):
        print('<'+tok.type+', '+str(tok.lineno)+', '+str(tok.lexpos)+'>')
    else:
        print('<'+tok.type+', '+tok.value+', ' +
              str(tok.lineno)+', '+str(tok.lexpos)+'>')
