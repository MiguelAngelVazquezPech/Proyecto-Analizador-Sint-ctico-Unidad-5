import ply.yacc as yacc
from analizador_lexico import tokens #herencia de los tokens del analizador lexico
import re 

# resultado del analisis
resultado_gramatica = []

#Aqui se colocan  los tokens heredados con su nivel de precedencia
precedence = (
    ('right','IF', 'ELSE'),
    ('left', 'SEMI'),
    ('left', 'COMMA'),
    ('left', 'ASIGNAR'),
    ('left', 'SEMI'),
    ('left', 'NE'),
    ('left', 'LT', 'LE','GT', 'GE', 'AS'),
    ('left', 'MAS','MENOS'),
    ('left', 'MULTI','DIVIDE'),
    ('left', 'LBRACE', 'RBRACE'),
    ('left', 'PARENTESISIZQ', 'PARENTESISDER')
)

#Almacena los tipos de asignacion
nombres = {}


#Estas funciones se definen las condicionales
def p_declaracion_coditionif(t):
    'declaracion : IF PARENTESISIZQ expresion GT expresion PARENTESISDER LBRACE expresion SEMI RBRACE'
    t[0] = t[1] # en dado caso que se quiera reutilizar solo se cambian los tokens con referencia la leguaje

#declaracion de funcion else
def p_declaracion_coditionelse(t):
    'declaracion : ELSE LBRACE expresion SEMI RBRACE'
    t[0] = t[1]

# se definde como se debe llevar el proceso de asignacion con refencia al tipo de dato
def p_declaracion_asignar(t):
    'declaracion : INT expresion ASIGNAR expresion SEMI'
    nombres[t[1]] = t[3]

def p_declaracion_asignar2(t):
    'declaracion : DOUBLE expresion ASIGNAR expresion SEMI'
    nombres[t[1]] = t[3]
    
# se define como inicia el programa
def p_declaracion_taginicio(t):
    'declaracion : INICIO'
    t[0] = t[1]

# se define como concluye el programa
def p_declaracion_tagfinal(t):
    'declaracion :  FIN'
    t[0] = t[1]

#como se define una expresion.
def p_declaracion_expr(t):
    'declaracion : expresion SEMI'
    t[0] = t[1]


#definimos como se validara los operandos
def p_expresion_operaciones(t):
    '''
    expresion  :    expresion MAS expresion 
                |   expresion MENOS expresion 
                |   expresion MULTI expresion
                |   expresion DIVIDE expresion 

    '''
    #como debe de expresarse las operaciones cuando se este compilando 
    if t[2] == '+':
        t[0] = t[1] + t[3]
    elif t[2] == '-':
        t[0] = t[1] - t[3]
    elif t[2] == '*':
        t[0] = t[1] * t[3]
    elif t[2] == '/':
        t[0] = t[1] / t[3]

#variante de el menos
def p_expresion_minus(t):
    'expresion : MENOS expresion %prec MENOS'
    t[0] = -t[2]

#como se definen las expresiones entre parentesis y corchetes con expreciones
def p_expresion_grupo(t):
    '''
    expresion  : PARENTESISIZQ expresion PARENTESISDER 
                | LBRACE expresion RBRACE

    '''
    t[0] = t[2]

# sintactico de expresiones logicas
def p_expresion_logicas(t):
    '''
    expresion   :  expresion LT expresion 
                |  expresion GT expresion 
                |  expresion LE expresion 
                |   expresion GE expresion 
                |   expresion ASIGNAR expresion 
                |   expresion AS expresion
                |  PARENTESISIZQ expresion LT expresion PARENTESISDER
                |  PARENTESISIZQ expresion GT expresion PARENTESISDER
                |  PARENTESISIZQ expresion LE expresion PARENTESISDER
                |  PARENTESISIZQ expresion GE expresion PARENTESISDER
                |  PARENTESISIZQ expresion ASIGNAR expresion PARENTESISDER
                |  PARENTESISIZQ expresion AS expresion PARENTESISDER
    ''' #cada una de las variantes en las expresiones logicas
    if t[2] == "<":
        t[0] = t[1] < t[3]
    elif t[2] == ">":
        t[0] = t[1] > t[3]
    elif t[2] == "<=":
        t[0] = t[1] <= t[3]
    elif t[2] == ">=":
        t[0] = t[1] >= t[3]
    elif t[2] == "==":
        t[0] = t[1] is t[3]
    elif t[2] == "!=":
        t[0] = t[1] != t[3]
    elif t[3] == "<":
        t[0] = t[2] < t[4]
    elif t[2] == ">":
        t[0] = t[2] > t[4]
    elif t[3] == "<=":
        t[0] = t[2] <= t[4]
    elif t[3] == ">=":
        t[0] = t[2] >= t[4]
    elif t[3] == "==":
        t[0] = t[2] is t[4]
    elif t[3] == "!=":
        t[0] = t[2] != t[4]

#definicion de las funciones de tipos de variable, muy importante tomar en cuenta el orden 
def p_expresion_decimal(t):
    'expresion : DECIMAL'
    t[0] = t[1]

def p_expresion_numero(t):
    'expresion : NUMERO'
    t[0] = t[1]

def p_expresion_id(t):
    'expresion : ID'
    t[0] = t[1]

#funcion que nos ayuda a recibir el error en caso de existir
def p_error(t):
    global resultado_gramatica
    if t:
        resultado = "Error sintactico de tipo {:4} en el valor {:4}".format(
            str(t.type), str(t.value))
    else:
        resultado = "Error sintactico {}".format(t)
        
    resultado_gramatica.append(resultado)

# instanciamos el analizador sintactico
sintactico = yacc.yacc()

#funcion que captura de manera precisa los errores
def prueba_sintactica(data):
    global resultado_gramatica

    for item in data.splitlines():
        if item:
            gram = sintactico.parse(item)
            if gram:
                resultado_gramatica.append(str(gram))
        else:
            print("")         
    return resultado_gramatica



#importamos el archivo a analizar
dart = open('prueba.dart').read()
#impresion de los resultados de manera ordena.
prueba_sintactica(dart)
print('____________________________Analisis Sintactico____________________________')
print()
print('\n'.join(list(map(''.join, resultado_gramatica)))) 

