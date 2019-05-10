documento = open("documento.txt", "r")

lineas = documento.readlines()
#print([len(l) for l in lineas])
fila= 0
indice = 0

def siguiente_char():
    '''
    Esta funcion retorna el siguiente caracter en el documento y actualiza el valor de fila
    e indice, por lo que hay que tener cuenta que returna el caracter pero deja los valores de
    fila e indice actualizados para la siguiente vez que se llama a la funcion.
    '''
    global indice, fila
    a = lineas[fila][indice]
    if((indice) == (len(lineas[fila])-1)):
        fila += 1
        indice = 0
    else:
        indice += 1
    return a

""" for i in range(len(lineas)):
    for j in range(len(lineas[i])):
        print(siguiente_char()) """

