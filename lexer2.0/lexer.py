# Libreria para hacer uso de expresones regulares
import re

# archivo a utilizar como prueba
documento = open("/home/jann/Documents/UN/2019-1/Lenguajes/analizadorLexico/lexer2.0/documento.txt", "r")

# lista de todas las lineas que contiene el documento
lineas = documento.readlines()
documento.close()
fila = 0
indice = 0

#definicion de la clase token
class Token:

    def __init__(self, fila, columna, tipo, lexema):
        self.fila = fila
        self.columna = columna
        self.tipo =  tipo #Igual a una de las constantes
        self.lexema = lexema

    #Constantes
    ID = 1
    ENTERO = 2
    REAL = 3
    STRING = 4
    BOOLEANO = 5
    OPERADOR = 6
    PALABRA_RESERVADA = 7

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
def es_aceptado(indice, fila):
    aux_indice = indice
    aux_fila = fila
    auxii=""
    a = lineas[aux_fila][aux_indice]
    if((aux_indice) == (len(lineas[aux_fila])-1)):
        aux_fila += 1
        aux_indice = 0
    else:
        auxii += a
        while(True):
            if(aux_fila == len(lineas)):
                break
            if((aux_indice) == (len(lineas[aux_fila])-1)):
                break
            else:
                auxii += a
                if(es_valido_para(ER_indentificador, auxii)):
                    while(es_valido_para(ER_indentificador, auxii)):
                        aux_indice += 1
                        if ((aux_indice) == (len(lineas[aux_fila])-1)):
                            break
                        a = lineas[aux_fila][aux_indice]
                        auxii += a

    return [auxii, aux_fila, aux_indice]

""" def es_numero(n):
    if(siguiente_char[0]==ER_Entero):
        return True

 """

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
    'verdadero': '<verdadero, ',
    'TRUE': '<TRUE, ',
    'FALSE': '<FALSE, '

}
# EXPRESIONES REGULARES
ER_indentificador = r'\w'  # Regex para caracter identificador
ER_digito = r'\d'  # Regex para digitos
ER_Entero = r'[-?\d]+'


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


print(es_aceptado(0,0))


def analex():
    c = siguiente_char()
    if((c[0] == ' ' or c[0] == '\t' or c[0] == '\n')):
        return

#---NOTA---: REVISAR PRESENTACIONES DEL PROFESOR, ES LA GUIA PARA ANALISIS
# LEXICO CARACTER POR CARACTER