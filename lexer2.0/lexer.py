# Libreria para hacer uso de expresones regulares
import re

# archivo a utilizar como prueba
documento = open(
    "/home/jann/Documents/UN/2019-1/Lenguajes/analizadorLexico/lexer2.0/documento.txt", "r")

# lista de todas las lineas que contiene el documento
lineas = documento.readlines()
documento.close()
fila = 0
indice = 0


def siguiente_char():
    '''
    Esta funcion retorna el siguiente caracter en el documento y actualiza el valor de fila
    e indice, por lo que hay que tener cuenta que returna el caracter pero deja los valores de
    fila e indice actualizados para la siguiente vez que se llama a la funcion.
    '''
    global indice, fila
    fila_aux, indice_aux = fila, indice
    a = lineas[fila][indice]
    if((indice) == (len(lineas[fila])-1)):
        fila += 1
        indice = 0
    else:
        indice += 1
    return [a, fila_aux, indice_aux]


""" Prueba
    for i in range(len(lineas)):
        for j in range(len(lineas[i])):
            print(siguiente_char()) """

palabras_reservadas = {
    'and': '<and, ',
    'constantes': '<constantes,',
    'hasta': '<hasta, ',
    'matriz': '<matriz, ',
    'paso': '<paso, ',
    'regitro': '<registro, ',
    'sino': '<sino, ',
    'vector': '<vector, ',
    'archivo': '<archivo, ',
    'desde': '<desde, ',
    'inicio': '<inicio, ',
    'mientras': '<mientras, ',
    'subrutina': '<subrutina, ',
    'repetir': '<repetir, ',
    'tipos': '<tipos, ',
    'caso': '<caso, ',
    'eval': 'eval, ',
    'lib': '<lib, ',
    'not': '<not, ',
    'programa': '<programa, ',
    'retorna': '<retorna, ',
    'var': '<var, ',
    'const': '<const, ',
    'fin': '<fin, ',
    'libext': '<libext, ',
    'or': '<or, ',
    'ref': '<ref, ',
    'si': '<si, ',
    'variables': '<variables, ',
    'numerico': '<numerico, ',
    'imprimir': '<imprimir, ',
    'leer': '<leer, ',
    'dim': '<dim, ',
    'cls': '<cls, ',
    'set_ifs': '<set_ifs, ',
    'abs': '<abs, ',
    'arctan': '<arctan, ',
    'ascii': '<ascii, ',
    'cos': '<cos, ',
    'dec': '<dec, ',
    'eof': '<eof, ',
    'exp': '<exp, ',
    'get_ifs': '<get_ifs, ',
    'inc': '<inc, ',
    'int': '<int, ',
    'log': '<log, ',
    'lower': '<lower, ',
    'mem': '<mem, ',
    'ord': '<ord, ',
    'paramval': '<paramval, ',
    'pcount': '<pcount, ',
    'pos': '<pos, ',
    'random': '<random, ',
    'sec': '<sec, ',
    'set_stdin': '<set_stdin, ',
    'set_stdout': '<set_stdout, ',
    'sin': '<sin, ',
    'sqrt': '<sqrt, ',
    'srt': '<srt, ',
    'strdup': '<strdup, ',
    'strlen': '<strlen, ',
    'tan': '<tan, ',
    'upper': '<upper, ',
    'val': '<val, ',
    'logico': '<logico, ',
    'verdadero': '<verdadero, '
}
# EXPRESIONES REGULARES
ER_indentificador = r'[\wñÑ]'  # Regex para caracter identificador
ER_digito = r'\d'  # Regex para digitos


def es_valido_para(ER, caracter):
    ''' funcion para verificar si es un caracter que cumple con un ER dado '''
    return re.search(ER, caracter) != None


"""
a = '_'
PRUEBA para saber mirar si empieza en numero o no un identificador
if(es_valido_para(ER_indentificador, a) and not(es_valido_para(ER_digito, a))):
    print('Haga esto')
else:
    print('Haga aquello')

PRUEBA print(es_valido_para(ER_indentificador, '1'))
"""

# Logica para iterar a traves de las lineas por medio de sus indices
longitud = 0  # longitud total
longitudes = [len(i) for i in lineas]  # arreglo de longitudes de cada linea
# PRUEBA: print(longitudes)

# calculo de la longitud total del documento.
for i in range(len(longitudes)):
    longitud += longitudes[i]
#PRUEBA: print(longitud)

""" PRUEBA:  for i in range(longitud):
    print(siguiente_char()) """


#---NOTA---: REVISAR PRESENTACIONES DEL PROFESOR, ES LA GUIA PARA ANALISIS
# LEXICO CARACTER POR CARACTER