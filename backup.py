import re
'''
Library for using regular expresions
'''


full_path= ['0.txt', 'tu/path/hacia/el/archivo']

'''
f reads the .txt file with the code
document stores the whole file as a string
'''
f = open(full_path[0], 'r')
document = f.read()
f.close()

#Regular expresions list
RE_identifier = r'[a-zA-ZñÑ][\wñÑ]*'
RE_numbers = r'((\+|\-)?\d+(\.\d+)?((e|E)(\+|\-)\d+)?)'
#RE_multiline_comment = r'\/\*(.|\n)*\*\/'
#RE_single_line_comment = r'\/\/.*'
RE_comment= r'((\/\*(.|\n)*\*\/)|(\/\/.*))'
#RE_string_single_quote = r"'((\\')|(\n)|[^\'])*'"
#RE_string_double_quotes = r'"((\\")|(\n)|[^\"])*"'
RE_string = r"((\'((\\\')|(\n)|[^\'])*\')|(\"((\\\")|(\n)|[^\"])*\"))"
RE_operators_of_two_chars = r'(<=|>=|==|<>)'
RE_operators_of_one_char = r'(=|\+|\-|\*|\/|%|\^|,|\.|;|:|\[|\]|\{|\}|\(|\)|<|>)'
RE_errors = r'([^\s])'
RE_filas_columnas = r'(\d+), (\d+)'
RE_tokens =  r'^<.*, (.*,)?(\d+), (\d+)>$'


reserved_words = {
  'and': '<and, ',
  'constantes' : '<constantes, ',
  'hasta' : '<hasta, ',
  'matriz' : '<matriz, ',
  'paso' : '<paso, ',
  'regitro' : '<registro, ',
  'sino' : '<sino, ',
  'vector' : '<vector, ',
  'archivo' : '<archivo, ',
  'desde' : '<desde, ',
  'inicio' : '<inicio, ',
  'mientras' : '<mientras, ',
  'subrutina' :'<subrutina, ',
  'repetir' : '<repetir, ',
  'tipos' : '<tipos, ',
  'caso' : '<caso, ',
  'eval' : 'eval, ',
  'lib' : '<lib, ',
  'not': '<not, ',
  'programa' : '<programa, ',
  'retorna' : '<retorna, ',
  'var' : '<var, ',
  'const' : '<const, ',
  'fin' : '<fin, ',
  'libext' : '<libext, ',
  'or' : '<or, ',
  'ref' : '<ref, ',
  'si' : '<si, ',
  'variables' : '<variables, ',
  'numerico' : '<numerico, ',
  'imprimir' : '<imprimir, ',
  'leer': '<leer, ',
  'dim' : '<dim, ',
  'cls' : '<cls, ',
  'set_ifs' : '<set_ifs, ',
  'abs' : '<abs, ',
  'arctan' : '<arctan, ',
  'ascii' : '<ascii, ',
  'cos' : '<cos, ',
  'dec' : '<dec, ',
  'eof' : '<eof, ',
  'exp' : '<exp, ',
  'get_ifs' : '<get_ifs, ',
  'inc' : '<inc, ',
  'int' : '<int, ',
  'log' : '<log, ',
  'lower' : '<lower, ',
  'mem' : '<mem, ',
  'ord' : '<ord, ',
  'paramval' : '<paramval, ',
  'pcount' : '<pcount, ',
  'pos' : '<pos, ',
  'random' : '<random, ',
  'sec' : '<sec, ',
  'set_stdin' : '<set_stdin, ',
  'set_stdout' : '<set_stdout, ',
  'sin' : '<sin, ',
  'sqrt' : '<sqrt, ',
  'srt' : '<srt, ',
  'strdup' : '<strdup, ',
  'strlen' : '<strlen, ',
  'tan' : '<tan, ',
  'upper' : '<upper, ',
  'val' : '<val, ',
  'logico' : '<logico, ',
  'verdadero' : '<verdadero, '
}

reserved_operation = {
  '.' : '<tk_punto, ',
  ',' : '<tk_coma, ',
  ':' : '<tk_dospuntos, ',
  '(' : '<tk_par_izq, ',
  ')' : '<tk_par_der, ',
  ';' : '<tk_punto_y_coma, ',
  '=' : '<tk_asig, ',
  '{' : '<tk_llave_izq, ',
  '}' : '<tk_llave_der, ',
  '[' : '<tk_corchete_izq, ',
  ']' : '<tk_corchete_der, ',
  '<>' : '<tk_distinto, ',
  '==' : '<tk_igual_que, ',
  '<' : '<tk_menor_que, ',
  '>' : '<tk_mayor_que, ',
  '<=' : '<tk_menor_igual_que, ',
  '>=' : '<tk_mayor_igual_que, ',
  '^' : '<tk_potenciacion, ',
  '%' : '<tk_modulo, ',
  '/' : '<tk_division, ',
  '+' : '<tk_suma, ',
  '-' : '<tk_resta, ',
  '*' : '<tk_multiplicacion, ',
}
unknown_words = {
  'cadena': '<tk_cadena, ',
  'id' : '<id, ',
  'numero' : '<tk_num, '
}

#lista a ordenar de los tokens obtenidos
tokens_unsorted = []

#paso 1,2 evaluar ER para strings|comentarios devolviendo un arreglo de findall

def obtener_array_de_matches(archivo, regex):
  '''
  This function returns an array containing all the matches for a regular expression in a given
  string (the string containing the file previously read)
  '''
  file = archivo
  array = []
  while(True):
    first_match = re.search(regex, file)
    if(first_match == None):
      break
    else:
      array.append(first_match.group())
      file = re.sub(regex, len(first_match.group())*' ', file,1)
  return array

#Prueba

"""
a = obtener_array_de_matches(document, RE_multiline_comment)
print(a)
"""


# Paso 3 Buscar para cada string en el arreglo 1, si esta contenido en alguno del arreglo 2, en caso de que si
#sacar dicho string de el arreglo 1 (esto para quitar los string que esten dentro de un comentario de la lista
# de strings)

def eliminar_cadenas(cadenas_a_eliminar, cadenas_a_evaluar):
  '''
  This function drops all the elements of the first array that are substrings from one
  element of the second array and returns a new array without the dropped ones.
  '''
  aux = []
  for i in range(len(cadenas_a_eliminar)):
    for j in range(len(cadenas_a_evaluar)):
      if (cadenas_a_evaluar[j].find(cadenas_a_eliminar[i]) != -1):
        aux.append(cadenas_a_eliminar[i])
        break
  i = 0
  while (i < len(aux)):
    cadenas_a_eliminar.remove(aux[i])
    i += 1
  return cadenas_a_eliminar

#Prueba
'''
a = ["'asdf'", "'asasas'", "'ssss'"]
b = ["//aa'asdf'", "/*  'asasas'*/", "//fafafa", "/* rerere */" ]
a = eliminar_cadenas(a, b)
print(a)
'''

#Paso 4.1 y 4.2

def obtener_fila_y_columna(path_al_archivo, inicio_de_cadena):
    f = open(path_al_archivo, 'r')
    array_de_lineas = f.readlines()
    array_without_enters = []
    c = 1
    for i in array_de_lineas:
      if(i == array_de_lineas[len(array_de_lineas)-1] and i != '\n'):
        if c == 1:
          array_without_enters.append(i)
          break
        else:
          array_without_enters.append('\n'+i)
          break
      if (c == 1):
        array_without_enters.append(i[:-1])
      else:
        array_without_enters.append('\n'+i[:-1])
      c += 1
    fila = 1
    columna=1
    aux = inicio_de_cadena
    for i in array_without_enters:
      if ( aux - len(i) < 0):
        if(inicio_de_cadena == 0):
          columna = 1
        else:
          columna = aux
        break
      else:
        fila += 1
        aux = aux - len(i)
    return [fila, columna]

#Prueba
'''
print(obtener_fila_y_columna('pruebas.txt', 12))
'''

def enlistar_y_reemplazar_string(objeto_de_match):
  fila_columna = obtener_fila_y_columna('pruebas.txt', objeto_de_match.span()[0])
  tokens_unsorted.append(unknown_words['cadena']+objeto_de_match.group()+', '+str(fila_columna[0])+', '+str(fila_columna[1])+'>')
  #guardar el token con la fila y columna indicada usando la funcion para
  # para encontrar ese valor
  return (len(objeto_de_match.group())*' ')

#Prueba
'''
whit the proff of eliminar_string this function is proved too.
'''
def eliminar_comentarios(RE, document):
  file = document
  while (True):
    first_match = re.search(RE, file)
    if(first_match == None):
      return file
      break
    else:
        file = re.sub(RE,len(first_match.group())*' ',file, 1)
  return file
def eliminar_comentarios_s(strings_array, document, RE):
  file = document
  while (True):
    first_match = re.search(RE, file)
    if(first_match == None):
      return file
      break
    else:
      for i in strings_array:
        if (i.find(first_match.group()) == -1):
          file = re.sub(RE,len(first_match.group())*' ',file, 1)
  return file

# Prueba
'''
a = obtener_array_de_matches(document, RE_string_double_quotes)
print(a)
b = obtener_array_de_matches(document, RE_multiline_comment)
print(b)
a = eliminar_cadenas(a, b)
c = eliminar_comentarios(a, document, RE_multiline_comment)
print( c)
'''

def eliminar_strings(RE, document):
  file = document
  while (True):
    first_match = re.search(RE, file)
    if(first_match == None):
      return file
      break
    else:
      file = re.sub(RE,enlistar_y_reemplazar_string,file, 1)
  return file

#Prueba
'''
print(eliminar_strings(RE_string_single_quote, document))
print(tokens_unsorted)
'''


def enlistar_y_reemplazar_identificador(objeto_de_match):
  fila_columna = obtener_fila_y_columna('pruebas.txt', objeto_de_match.span()[0])
  tokens_unsorted.append(unknown_words['id']+objeto_de_match.group()+', '+str(fila_columna[0])+', '+str(fila_columna[1])+'>')
  return (len(objeto_de_match.group())*' ')


def enlistar_y_reemplazar_palabra_reservada(objeto_de_match):
  fila_columna = obtener_fila_y_columna('pruebas.txt', objeto_de_match.span()[0])
  tokens_unsorted.append(reserved_words[objeto_de_match.group()]+str(fila_columna[0])+', '+str(fila_columna[1])+'>')
  return (len(objeto_de_match.group())*' ')

def eliminar_identificadores_y_palabras_reservadas(RE, document):
  file =  document
  while(True):
    first_match = re.search(RE, file)
    if (first_match == None):
      return file
      break
    else:
      if(reserved_words.get(first_match.group()) != None):
        file = re.sub(RE,enlistar_y_reemplazar_palabra_reservada,file, 1)
      else:
        file = re.sub(RE,enlistar_y_reemplazar_identificador,file, 1)
  return file

#Prueba
'''
print(eliminar_identificadores_y_palabras_reservadas(RE_identifier, document))
print(tokens_unsorted)
'''

def enlistar_y_reemplazar_numero(objeto_de_match):
  fila_columna = obtener_fila_y_columna('pruebas.txt', objeto_de_match.span()[0])
  tokens_unsorted.append(unknown_words['numero']+objeto_de_match.group()+', '+str(fila_columna[0])+', '+str(fila_columna[1])+'>')
  return (len(objeto_de_match.group())*' ')

def eliminar_numeros (RE, document):
  file = document
  while(True):
    first_match = re.search(RE, file)
    if (first_match == None):
      return file
      break
    else:
      file = re.sub(RE, enlistar_y_reemplazar_numero, file, 1)
  return file

#prueba
'''
print(eliminar_numeros(RE_numbers, document))
print(tokens_unsorted)
'''
def enlistar_y_reemplazar_operador_doble(objeto_de_match):
  fila_columna = obtener_fila_y_columna('pruebas.txt', objeto_de_match.span()[0])
  tokens_unsorted.append(reserved_operation[objeto_de_match.group()]+str(fila_columna[0])+', '+str(fila_columna[1])+'>')
  return (len(objeto_de_match.group())*' ')

def eliminar_operadores_dobles(RE, document):
  file = document
  while(True):
    first_match = re.search(RE, file)
    if (first_match == None):
      return file
      break
    else:
      file = re.sub(RE, enlistar_y_reemplazar_operador_doble, file, 1)
  return file


def enlistar_y_reemplazar_operador_sencillo(objeto_de_match):
  fila_columna = obtener_fila_y_columna('pruebas.txt', objeto_de_match.span()[0])
  tokens_unsorted.append(reserved_operation[objeto_de_match.group()]+str(fila_columna[0])+', '+str(fila_columna[1])+'>')
  return (len(objeto_de_match.group())*' ')

def eliminar_operadores_sencillos(RE, document):
  file = document
  while(True):
    first_match = re.search(RE, file)
    if (first_match == None):
      return file
      break
    else:
      file = re.sub(RE, enlistar_y_reemplazar_operador_sencillo, file, 1)
  return file


def enlistar_y_eliminar_error(objeto_de_match):
  fila_columna = obtener_fila_y_columna('pruebas.txt', objeto_de_match.span()[0])
  tokens_unsorted.append('<token_error, '+objeto_de_match.group()+', '+str(fila_columna[0])+', '+str(fila_columna[1])+'>')
  return (len(objeto_de_match.group())*' ')
def eliminar_errores(RE, file):
  file = document
  while(True):
    first_match = re.search(RE, file)
    if (first_match == None):
      return file
      break
    else:
      file = re.sub(RE, enlistar_y_eliminar_error, file, 1)
  return file

## inicio de la ejecucion
#print(document)
#print('-'*40)
a = obtener_array_de_matches(document, RE_string)
b = obtener_array_de_matches(document, RE_comment)
if len(a) == 0:
  document = eliminar_comentarios(RE_comment, document)
else:
  a = eliminar_cadenas(a,b)
  document = eliminar_comentarios_s(a,document,RE_comment)

#print(document)
#print('-'*40)
document = eliminar_strings(RE_string, document)
#print(document)
#print('-'*40)
document = eliminar_identificadores_y_palabras_reservadas(RE_identifier,document)
#print(document)
#print('-'*40)
document = eliminar_numeros(RE_numbers, document)
#print(document)
#print('-'*40)
document = eliminar_operadores_dobles(RE_operators_of_two_chars, document)
#print(document)
#print('-'*40)
document = eliminar_operadores_sencillos(RE_operators_of_one_char, document)
#print(document)
#print('-'*40)
document = eliminar_errores(RE_errors, document)
lista_auxiliar = tokens_unsorted
arreglo_de_f_y_c = []
def cambiar_numeros(objeto_de_match):
  arreglo_de_f_y_c.append([int(objeto_de_match.group(2)), int(objeto_de_match.group(3))])
  return 'abc'

for i in lista_auxiliar:
  first_match = re.search(RE_tokens, i)
  i = re.sub(RE_tokens, cambiar_numeros, i)

#print(arreglo_de_f_y_c)
#aux = []
#aux2 = []
lista_de_listas= []
lista_de_listas2 = []

for i in range(len(arreglo_de_f_y_c)):
  aux = []
  aux2 = []
  for j in range(len(arreglo_de_f_y_c)):
    if arreglo_de_f_y_c[j][0] == i+1:
      #print(arreglo_de_f_y_c[j])
      aux.append(arreglo_de_f_y_c[j])
      aux2.append(tokens_unsorted[j])
  #print(aux)
  if(aux != []):
    lista_de_listas.append(aux)
    lista_de_listas2.append(aux2)



def bubblesort(list1, list2):

    for iter_num in range(len(list1)-1,0,-1):
        for idx in range(iter_num):
            if list1[idx][1]>list1[idx+1][1]:
                temp = list1[idx]
                temp2 = list2[idx]
                list1[idx] = list1[idx+1]
                list2[idx] = list2[idx+1]
                list1[idx+1] = temp
                list2[idx+1] = temp2

#print(lista_de_listas)
for i in range(len(lista_de_listas)):
  bubblesort(lista_de_listas[i], lista_de_listas2[i])
#print(lista_de_listas)
#print(lista_de_listas2)
lista_ordenada= []
for i in lista_de_listas2:
  for j in i:
    lista_ordenada.append(j)

def error_final(objeto_de_match):
  print('>>>Error lexico(linea: '+objeto_de_match.group(1),'posicion: '+objeto_de_match.group(2)+')')
  return ' '
for i in lista_ordenada:
  if(i.find('<token_error, ') == -1):
    print(i)
  else:
    first_match = re.sub(RE_filas_columnas,error_final,i,1)
    break