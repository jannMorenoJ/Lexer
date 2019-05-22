def abrir_y_listar():
    f = open('./tokens/prueba.txt', 'r')
    arr = f.readlines()
    for i in range(len(arr)):
        aux = arr[i]
        aux = aux[:-1]
        arr[i] = aux
    f.close()
    return arr


def get_next_token(lista_tokens):
    return lista_tokens.pop(0)


def get_proximo_token(lista_tokens):
    return lista_tokens[0]


def emparejar():
    if(token == tok_esperado):
        token = lexico.get_next_token()
    else:
        errorSintaxis(tok_esperado)
    return


# Lista de tokens
tokens = abrir_y_listar()
# aqui solo se almacenara solo el tipo de token mas no su lexema o ubicacion
tipos_de_token = []


def obtener_lexema(cadena):
    '''
    Esta funcion se utiliza para obtener el tipo de token de un token dado
    '''
    arr = cadena.split(',')
    return arr[0][1:len(arr[0])]


# cargando los tipos de tokens en el arreglo tipos_de_tokens
for i in range(len(tokens)):
    tipos_de_token.append(obtener_lexema(tokens[i]))


# Reglas de la gramatica
# simbolo inicial de la gramatica

# nor7402 and7411 or4072b xor7486
token = get_next_token(tipos_de_token)


def A():
    reglas = [[B, 'uno'], ['dos']]
    aux = token()
    if(aux == 'tres' or aux == 'cuatro'):
        reglas[0][0]()
        emparejar()
