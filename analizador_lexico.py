full_path= ['/home/jann/Documents/UN/2019-1/Lenguajes/analizadorLexico/prueba.txt', 'tu/path/hacia/el/archivo']

'''
f reads the .txt file with the code
'''
f = open(full_path[0], 'r')

reserved_words = {
    'and': '<and,',
    'constantes' : '<constantes,',
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
    ',' : '<tk_coma,',
    ':' : '<tk_dospuntos, ',
    '(' : '<tk_par_izq, ',
    ')' : '<tk_par_der, ',
    ';' : '<tk_punto_y_coma, ',
    '=' : '<tk_asig, ',
    '{' : '<tk_llave_izq, ',
    '}' : '<tk_llave_der, ',
    '<>' : '<distinto, ',
    '==' : '<tk_igual_que, ',
    '<' : '<tk_menor_que, ',
    '>' : '<tk_mayor_que, ',
    '<=' : '<tk_menor_igual_que, ',
    '>=' : '<tk_mayor_igual_que, '

}

fila = 1

def leter_number_guionbajo(array, index):
    cero = 48
    nueve= 57
    A = 65
    Z = 90
    a = 97
    z = 122
    ene = 164
    ENE = 165
    guion_bajo = 95
    ascii = ord(array[index])
    if((ascii >= cero and ascii <= nueve ) or (ascii >= A and ascii <= Z) or (ascii >= a and ascii <= z) or (ascii == ene) or (ascii == ENE) or (ascii == guion_bajo)):
        return True
    else:
        return False

    ##preguntar al profesor como se identifican los identificadores, ejemplo uno de 100 caracteres, mandaria error? o devolveriamos 3 tokens?
for x in f:
    '''
    In this For loop we're going to execute our lexer logic.

    x => of type string, is the current line on the file.
    Some usefull code snippets are:
    len(x)
    x[n]
    ord(' ') for the ascii code for a character taken
    etc
    '''
    columna = 1
    for columna in range(len(x)):
        #codigo por linea
        if(reserved_words.get(x[columna])!= None):
            print(reserved_words.get(x[columna])+str(fila)+', '+str(columna+1)+'>')
            # else if()
        columna =+ 1

    fila +=1





