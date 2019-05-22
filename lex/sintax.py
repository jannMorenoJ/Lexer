import ply3.ply.yacc as yacc
import os
import codecs
import re
from lexer import tokens
from sys import stdin

# definir la precedencia de los tokens
precedence = (
    ('left', 'or'),
    ('left', 'and'),
    ('left', 'not'),
    ('left', 'tk_igual_que', 'tk_distinto', 'tk_menor_que',
     'tk_mayor_que', 'tk_menor_igual_que', 'tk_mayor_igual_que'),
    ('left', 'tk_suma', 'tk_resta'),
    ('left', 'tk_multiplicacion', 'tk_modulo', 'tk_division'),
    ('left', 'tk_potenciacion')
)


def p_S(p):
    ''' S : Programa Declaraciones inicio Sentencias fin Subrutinas'''


def p_Programa1(p):
    ''' Programa : programa id'''


def p_Programa2(p):
    '''Programa : empty '''
    pass


def p_Declaraciones1(p):
    ''' Declaraciones : Constantes Puntoycoma Declaraciones'''


def p_Declaraciones2(p):
    ''' Declaraciones : Tipos Puntoycoma Declaraciones'''


def p_Declaraciones3(p):
    ''' Declaraciones : empty'''
    pass


def p_Puntoycoma1(p):
    ''' Puntoycoma : tk_punto_y_coma'''


def p_Puntoycoma2(p):
    ''' Puntoycoma : empty'''
    pass


def p_Identificador(p):
    ''' Identificador : id Identificador2'''


def p_Identificador2(p):
    ''' Identificador2 : tk_punto id'''


def p_Identificador21(p):
    ''' Identificador2 : empty'''
    pass


def p_Constantes(p):
    ''' Constantes : const id tk_asig TiposConstantes Constantes2 '''


def p_Constantes2(p):
    ''' Constantes2 : id tk_asig TiposConstantes Constantes2'''


def p_Constantes21(p):
    ''' Constantes2 : empty'''


def p_TiposConstantes(p):
    ''' TiposConstantes : id  '''


def p_TiposConstantes1(p):
    ''' TiposConstantes : numerico'''


def p_TiposConstantes2(p):
    ''' TiposConstantes : logico'''


def p_TiposConstantes3(p):
    ''' TiposConstantes : tk_cadena'''


def p_EsNumero(p):
    ''' EsNumero : Identificador'''


def p_EsNumero1(p):
    ''' EsNumero : tk_numero'''


def p_EsNumero2(p):
    ''' EsNumero : tk_suma tk_numero'''


def p_EsNumero3(p):
    ''' EsNumero : tk_resta tk_numero'''


def p_EsNumero4(p):
    ''' EsNumero : OperacionMatematica'''


def p_EsNumero5(p):
    ''' EsNumero : LlamadoFuncion'''


def p_Dato1(p):
    ''' Dato : tk_cadena Dato2 '''


def p_Dato2(p):
    ''' Dato : EsNumero '''


def p_Dato3(p):
    ''' Dato : logico '''


def p_Dato4(p):
    ''' Dato : logico '''


def p_Dato5(p):
    ''' Dato : Estructura '''


def p_Dato6(p):
    ''' Dato : Registro'''


def p_Dato21(p):
    ''' Dato2 : tk_cadena'''


def p_Dato22(p):
    ''' Dato2 : empty'''
    pass


def p_Operador1(p):
    ''' Operador : tk_suma'''


def p_Operador2(p):
    ''' Operador : tk_resta'''


def p_Operador3(p):
    ''' Operador : tk_multiplicacion'''


def p_Operador4(p):
    ''' Operador : tk_division'''


def p_Operador5(p):
    ''' Operador : tk_modulo'''


def p_Operador6(p):
    ''' Operador : tk_potenciacion'''


def p_OperacionMatematica1(p):
    ''' OperacionMatematica : tk_par_izq OperacionMatematica tk_par_der OperacionMatematica2'''


def p_OperacionMatematica2(p):
    ''' OperacionMatematica : EsNumero OperacionMatematica2 '''


def p_OperacionMatematica3(p):
    ''' OperacionMatematica : Funcion OperacionMatematica2 '''


def p_OperacionMatematica21(p):
    ''' OperacionMatematica2 : Operador OperacionMatematica'''


def p_OperacionMatematica22(p):
    ''' OperacionMatematica2 : empty'''
    pass


def p_TipoDato1(p):
    ''' TipoDato : numerico'''


def p_TipoDato2(p):
    ''' TipoDato : cadena'''


def p_TipoDato3(p):
    ''' TipoDato : logico'''


def p_TipoDato4(p):
    ''' TipoDato : id'''


def p_TipoDato5(p):
    ''' TipoDato : Estructura'''


def p_TipoDato6(p):
    ''' TipoDato : Registro'''


def p_VariantesIgualdad(p):
    ''' VariantesIgualdad : tk_dospuntos tk_asig '''


def p_ListaId1(p):
    ''' ListaId : tk_coma id ListaId'''


def p_ListaId2(p):
    ''' ListaId : empty'''
    pass


def p_Variables(p):
    ''' Variables : id VariablesFix'''


def p_VariablesFix1(p):
    ''' VariablesFix : ListaId tk_dospuntos TipoDato Variables2 '''


def p_VariablesFix2(p):
    ''' VariablesFix : tk_asig Dato Variables2 '''


def p_Variables21(p):
    ''' Variables2 : id Variables2Fix '''


def p_Variables2Fix1(p):
    ''' Variables2Fix : ListaId tk_dospuntos TipoDato Variables2'''


def p_Variables2Fix2(p):
    ''' Variables2Fix : tk_asig Dato Variables'''


def p_Tipos(p):
    ''' Tipos : id tk_dospuntos TipoDato tipos'''


def p_Estructura1(p):
    ''' Estructura : vector tk_corchete_izq Dim1 tk_corchete_der TipoDato'''


def p_Estructura2(p):
    ''' Estructura : matriz tk_corchete_izq Dim tk_corchete_der TipoDato'''


def p_Dim11(p):
    ''' Dim1 :  tk_multiplicacion'''


def p_Dim12(p):
    ''' Dim1 :  numerico'''


def p_Dim(p):
    ''' Dim : Dim1 tk_coma Dim2'''


def p_Dim2(p):
    ''' Dim2 : Dim1 DimFix'''


def p_DimFix1(p):
    ''' DimFix : tk_coma'''


def p_DimFix2(p):
    ''' DimFix : empty'''
    pass


def p_Registro(p):
    ''' Registro : regitro tk_llave_izq Variables tk_llave_der '''


def P_Sentencias1(p):
    ''' Sentencias : LlamadoFuncion Sentencias'''


def p_Sentencias2(p):
    ''' Sentencias : EstructuraControl Sentencias'''


def p_sentencias3(p):
    ''' Sentencias : empty'''
    pass


def p_LlamadoFuncion(p):
    ''' LlamadoFuncion : id tk_par_izq Parametros tk_par_der'''


def p_Parametros1(p):
    ''' Parametros : Identificador ListaParametros'''


def p_Parametros2(p):
    ''' Parametros : LlamadoFuncion ListaParametros'''


def p_Parametros3(p):
    ''' Parametros : empty'''
    pass


def p_ListaParametros1(p):
    ''' ListaParametros : tk_coma Identificador ListaParametros'''


def p_ListaParametros2(p):
    ''' ListaParametros : tk_coma Dato ListaParametros'''


def p_ListaParametros3(p):
    ''' ListaParametros : tk_coma LlamadoFuncion ListaParametros'''


def p_ListaParametros4(p):
    ''' ListaParametros : empty'''
    pass


def p_Asignacion(p):
    ''' Asignacion : Identificador tk_asig Dato'''


def p_EstructuraControl(p):
    ''' EstructuraControl : If Mientras RepetirHasta Desde Eval '''

# Aqui empieza la parte de Laura


def p_ListaMatrices1(p):
    '''ListaMatrices : tk_coma MatrizInit ListaMatrices'''


def p_ListaMatrices2(p):

'''ListaMatrices : tk_coma tk_tres_puntos'''


def p_ListaMatrices3(p):

'''ListaMatrices : empty'''
pass


def p_ListaVector1(p):

'''ListaVector : tk_coma VectorInit ListaVector'''


def p_ListaVector2(p):


'''ListaVector : tk_coma tk_tres_puntos'''


def p_ListaVector3(p):

'''ListaVector : empty'''
pass


def p_MatrizInit(p):

'''MatrizInit : tk_llave_izq VectorInit ListaVector tk_llave_der'''


def p_ListaDatos1(p):

'''ListaDatos : empty'''
pass


def p_ListaDatos2(p):

'''ListaDatos : tk_coma Dato ListaDatos'''


def p_ValoresVector1(p):

'''ValoresVector : Dato ListaDatos'''


def p_ValoresVector2(p):

'''ValoresVector : tk_coma tk_tres_puntos'''


def p_ValoresVector3(p):

'''ValoresVector : empty'''
pass


def p_VectorInit(p):

'''VectorInit : tk_llave_izq ValoresVector tk_llave_der'''


def p_ListaParametrosSubrutina1(p):

'''ListaParametrosSubrutina : empty'''
pass


def p_ListaParametrosSubrutina2(p):

'''ListaParametrosSubrutina : id tk_dospuntos TipoDato ListaParametrosSubrutina'''


def p_ParametrosSubrutina1(p):

'''ParametrosSubrutina : empty'''
pass


def p_ParametrosSubrutina2(p):

'''ParametrosSubrutina : id tk_dospuntos TipoDato ListaParametrosSubrutina'''


def p_ParametrosSubrutina3(p):

'''ParametrosSubrutina : ref id tk_dospuntos TipoDato ListaParametrosSubrutina'''


def p_Funcion(p):

'''Funcion : subrutina id tk_par_izq ParametrosSubrutina tk_par_der retorna tk_par_izq id Declaraciones inicio Sentencias retorna tk_par_izq id tk_par_der fin Subrutinabase'''


def p_Metodo(p):

'''Metodo : subrutina id tk_par_izq ParametrosSubrutina tk_par_der Declaraciones inicio Sentencias fin Subrutinabase'''


def p_Subrutinabase1(p):

'''Subrutinabase : Metodo'''


def p_Subrutinabase2(p):

'''Subrutinabase : Funcion'''


def p_Subrutinabase3(p):

'''Subrutinabase : empty'''
pass


def p_OperadorComparacion1(p):

'''OperadorComparacion : tk_mayor_igual_que'''


def p_OperadorComparacion2(p):

'''OperadorComparacion : tk_menor_igual_que'''


def p_OperadorComparacion3(p):

'''OperadorComparacion : tk_igual_que'''


def p_OperadorComparacion4(p):

'''OperadorComparacion : tk_mayor_que'''


def p_OperadorComparacion5(p):

'''OperadorComparacion : tk_menor_que'''


def p_OperadorComparacion6(p):

'''OperadorComparacion : tk_distinto'''


def p_ValoresComparacion1(p):

'''ValoresComparacion : id'''


def p_ValoresComparacion2(p):

'''ValoresComparacion : tk_numero'''


def p_ValoresComparacion3(p):

'''ValoresComparacion : logico'''


def p_ValoresComparacion4(p):

'''ValoresComparacion : cadena'''


def p_Comparacion(p):
    '''Comparacion : ValoresComparacion OperadorComparacion ValoresComparacion'''


def p_ExpresionLogica21(p):
    '''ExpresionLogica2 : and ExpresionLogica'''


def p_ExpresionLogica22(p):
    '''ExpresionLogica2 : or ExpresionLogica'''


def p_ExpresionLogica23(p):
    '''ExpresionLogica2 : empty'''
pass


def p_ExpresionLogica1(p):
    '''ExpresionLogica : logico ExpresionLogica2'''


def p_ExpresionLogica2(p):
    '''ExpresionLogica : id ExpresionLogica2'''


def p_ExpresionLogica3(p):
    '''ExpresionLogica : not ExpresionLogica ExpresionLogica2'''


def p_ExpresionLogica4(p):
    '''ExpresionLogica : Funcion ExpresionLogica2'''


def p_ExpresionLogica5(p):
    '''ExpresionLogica : Comparacion ExpresionLogica2'''


def p_ExpresionLogica6(p):
    '''ExpresionLogica : tk_par_izq ExpresionLogica tk_par_der ExpresionLogica2'''


def p_Eval(p):
    '''Eval : eval tk_llave_izq Casos Sino tk_llave_der'''


def p_Casos1(p):
    '''Casos : caso tk_par_izq Condicion tk_par_der Sentencias Casos'''


def p_Casos2(p):
    '''Casos : empty'''
    pass


def p_Sino1(p):
    '''Sino : sino tk_par_izq Condicion tk_par_der Sentencias'''


def p_Sino2(p):
    '''Sino : empty'''
pass


def p_Paso1(p):
    '''Paso : empty'''
pass


def p_Paso2(p):
    '''Paso : paso EsNumero'''


def p_Desde(p):
    '''Desde : desde id tk_asig EsNumero hasta EsNumero Paso tk_llave_izq Sentencias tk_llave_der'''


def p_RepetirHasta(p):
    '''RepetirHasta : repetir Sentencias hasta tk_par_izq Condicion tk_par_der'''


def p_Mientras(p):
    '''Mientras : mientras tk_par_izq Condicion tk_par_der tk_llave_izq Sentencias tk_llave_der'''


def p_Aux(p):
    '''Aux : sino Aux2'''


def p_Aux21(p):
    '''Aux2 : Sentencias tk_llave_der'''


def p_Aux22(p):
    '''Aux2 : si Sentencias Aux3'''


def p_Aux31(p):
    '''Aux3 : Aux'''


def p_Aux32(p):
    '''Aux3 : Sino tk_llave_der'''


def p_If(p):
    '''If : si tk_par_izq Condicion tk_par_der tk_llave_izq Sentencias Aux'''
