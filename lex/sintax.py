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
    ''' Identificador'''
