#!/usr/bin/env python
'''
Condicionales [Python]
Ejercicios de clase
---------------------------
Autor: Inove Coding School
Version: 1.1
 
Descripcion:
Programa creado para poner a prueba los conocimientos adquiridos durante la clase
'''

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.1"

def ej1():
    # Ejercicios de práctica numérica
    
    # Comparadores
    # Ingrese dos números cualesquiera y realice las sigueintes
    # comparaciones entre ellos

    numero_1 = int(input('Ingrese el primer número:\n'))

    numero_2 = int(input('Ingrese el segundo número:\n'))
    
    # Compare cual de los dos números es mayor
    # Imprima en pantalla según corresponda
   
    if (numero_1 != numero_2) and (numero_1 > numero_2):
        print ( numero_1, 'es mayor que', numero_2)
   
    elif ( numero_1 == numero_2):
        print ( numero_2,'es igual', numero_1)
   
    else:
        print ( numero_2,'es mayor que', numero_1)

    # Verifique si el numero_1 positivo, negativo o cero
    # Imprima el resultado en cada caso
   
    if ( numero_1 == 0):
        print (' {} es igual a 0'.format( numero_1))
   
    elif ( numero_1 > 0):
        print ('{} es positivo'.format(numero_1))
   
    else:
        print ('{} es negativo'.format(numero_1))


    # Verifique si el numero_1 es mayor a 0 y menor a 100
    # Imprima en pantalla si se cumple o no la condición

    # Inove: En el siguiente ejercicio podría haber sido 
    # suficiente colocar la primera sentencia condicional:
    # if (numero_1 > 0) and (numero_1 < 100) 
    # ya que de esa forma se esta verificando si:
    # el "numer_1" es mayor (>) a 0" y (and) el numero_1 es menor (<) a 100
    # me gustaría que puedas explicarme con tus palabras la razón de la condición
    # agregada del "o" (or)
    
    if (numero_1 > 0) and (numero_1 < 100) or (numero_1 == 100) and (numero_1 > 100):
        print ('{} es mayor que 0 y menor que 100' .format(numero_1))
   
    elif (numero_1 == 0) or (numero_1 < 0):
        print ('{} es 0 o menor' .format(numero_1))
   
    elif (numero_1 == 100) or (numero_1 > 100):
        print ('{} es 100 o mayor' .format(numero_1))

    # Verifique si el numero_1 es menor a 10 o el numero_2
    # es mayor a -2
    # Imprima en pantalla si se cumple o no la condición
    if ( numero_1 < 10) and (numero_2 > -2):
        print ('{} es menor a 10 y {} es mayor a -2' .format(numero_1, numero_2))
    
    elif ( numero_1 <10) and (numero_2 < -2):
        print ('{} es menor a 10 pero {} es menor a -2' .format(numero_1, numero_2))
    
    elif (numero_1 > 10) and (numero_2 > -2):
        print ('{} es mayor a 10 pero {} es mayor a -2' .format(numero_1, numero_2))
    
    else:
        print ('{} es mayor a 10 y {} es menor a -2'.format(numero_1, numero_2))

def ej2():
    # Ejemplos variables de texto

    # Comparadores
    # Ingrese dos palabras cualesquiera y realice las sigueintes
    # comparaciones entre ellas
    texto_1 = str(input('Ingrese la primera palabra:\n'))

    texto_2 = str(input('Ingrese la segunda palabra:\n'))

    # Compare cual de las dos palabras es mayor (alfabéticamente)
    # Imprima en pantalla según corresponda

    if texto_1 > texto_2:
        print( texto_1, "es mayor alfabeticamente")
    
    elif texto_1 == texto_2 :
        print('Son iguales alfabeticamente')
    
    else:
        print( texto_2, "Es mayor alfabeticamente")

    # Compare cual de las dos palabras tiene mayor
    # cantidad de letras
    # Imprima en pantalla según corresponda
    
    if (len(texto_1) > len(texto_2)):
        print (texto_1, ' tiene mas letras que', texto_2)
    
    elif (len(texto_1) == len(texto_2)):
        print (texto_1, ' tiene las mismas letras que', texto_2)
    
    else:
        print ("{} tiene mas letras que {}" .format(texto_2, texto_1))

    # Verifique si la primera letra de la primera palabra
    # es mayor a la primera letra de la segunda palabra
    # Imprima en pantalla según corresponda
   
    caracter_1= texto_1[0]
    caracter_2 = texto_2[0]
    
    if ((caracter_1) > (caracter_2)):
        print (caracter_1, ' es mas grande que',caracter_2)

    elif (caracter_1) == (caracter_2):
        print ('Son la misma letra')
   
    else:
        print ("{} es mas grande que {}" .format( caracter_2, caracter_1))
   
    copia_texto_1 = texto_1  # Copia de la variable texto_1

    # Verifique que copia_texto_1 es igual a texto_1
    # Imprima en pantalla según corresponda
   
    if (copia_texto_1 == texto_1):
        print('Son la misma palabra')
    
    else:
        print('Son palabras diferentes')

    # Verifique que copia_texto_1 es distinta a texto_2
    # Imprima en pantalla según corresponda
    
    if(copia_texto_1 != texto_2):
        print('Son textos distintos')
    
    else:
        print ('Son los mismos textos')


def ej3():
    # Ejercicios de práctica numérica

    # Condicionales anidados
    numero_1 = 6
    numero_2 = -2

    # Verifique si el numero_1 es mayor a 5
    #   --> En caso afirmativo, verifique si el numero_2
    #       es positivo
    #       --> En caso afirmativo imprima en pantalla "Resp=1"
    #       --> En caso negativo imprima en pantalla   "Resp=2"
    #  --> En caso negativo (numero_1 no es mayor a 5) 
    #      verifique si el numero_2 es mayor a 5
    #       --> En caso afirmativo imprima en pantalla "Resp=3"
    #       --> En caso negativo imprima en pantalla "Resp=4"
    
    if (numero_1 > 5):
        if (numero_2 > 0):
            print ('resp=1')
        else:
            print ('resp=2')
    else:
        if(numero_2 > 5):
            print('resp=3')
        else:
            print('resp=4')
   

    # Verifique la calificación de un estudiante según su
    # puntaje en un examen
    puntaje = 50

    # Si el puntaje es mayor igual a 90 --> imprimir A
    # Si el puntaje es mayor igual a 80 --> imprimir B
    # Si el puntaje es mayor igual a 70 --> imprimir C
    # Si el puntaje es mayor igual a 60 --> imprimir D
    # Si el puntaje es manor a  60      --> imprimir F

    # Debe imprimir en pantalla la calificacion
    # Utilizar "if" anidados

    if (puntaje >= 90):
        print ('A')
    elif (puntaje >= 80):
        print ('B')
    elif (puntaje >= 70):
        print ('C')
    elif (puntaje >= 60):
        print ('D')
    else:
        print ('F')




def ej4():
    # Ejemplos variables de texto

    texto_1 = '5'
    texto_2 = '1'

    # Verifique cual cual de los dos textos es mayor alfabéticamente
    # Imprima en pantalla según corresponda

    if texto_1 > texto_2:
        print( texto_1, "es mayor alfabeticamente")
    
    elif texto_1 == texto_2 :
        print('Son iguales alfabeticamente')
    
    else:
        print( texto_2, "Es mayor alfabeticamente")

    # Transforma esas variables tipo texto y almacénalas
    # en nuevas variables númericas (int)
    
    numero_1 = int (texto_1)
    numero_2 = int (texto_2)
    
    # Repita el proceso, ¿Cuál de las nuevas variables es mayor?
    # Imprima en pantalla según corresponda
    
    if (numero_1 != numero_2) and (numero_1 > numero_2):
        print ( numero_1, 'es mayor que', numero_2)
   
    elif ( numero_1 == numero_2):
        print ( numero_2,'es igual', numero_1)
   
    else:
        print ( numero_2,'es mayor que', numero_1)

    # Para pensar!
    # ¿Por qué cree que texto_2 es mayor a texto_1?
    # Siendo números tiene sentido, pero son caracteres, texto,
    # aún así el operador arroja el mismo resultado que con las
    # variables numéricas, cierto? ¿Por qué creen que es así?
    # Esta pregunta estará repetida en el Campus para que puedan
    # responder.
    # NOTA: La respuesta no se encuentra en el apunte, sino en Google ;)


def ej5():
    # Ejercicios de práctica con números
       
    '''
    Realice un programa que solicite ingresar tres valores de temperatura
    De las temperaturas ingresadas por consola determinar:
    1 - ¿Cuáles de ellas es la máxima temperatura ingresada?
    2 - ¿Cuáles de ellas es la mínima temperatura ingresada?
    3 - ¿Cuál es el promedio de las temperaturas ingresadas?

    En cada caso imprimir en pantalla el resultado  

    '''

    tem_1 = int(input('Ingrese una temperatura:'))
    tem_2 = int(input('Ingrese la siguiente temperatura:'))
    tem_3 = int(input('Ingrese la ultima temperatura:'))
   
    temp_pro=((tem_2 + tem_3 + tem_1)/3)
    
    # Inove: En Python es correcta la sentencia lógica
    # tal como lo armaste, pero no en todos los lugares
    # podrás aplicar la sentencia en este formato.
    # Te recomiendo que para evitar un problema futuro
    # reemaplces esta forma de sentencia:
    # if (tem_1 > tem_2 and tem_3):
    # por la siguiente
    # if (tem_1 > tem_2) and (tem_1 > tem_3):
    # Lo mismo aplica para los otros casos
    
    if (tem_1 > tem_2 and tem_3):
        print('La tempertura maximas es {}  ' .format(tem_1))
    elif(tem_2 > tem_1 and tem_3):
        print('La temperatura maxima es {}  ' .format(tem_2))
    else:
        print('La temperatura maxima es {}  ' .format(tem_3))
    
    if (tem_1 < tem_2 and tem_3):
        print('La temperatura minima es {}' .format(tem_1))
    elif(tem_2 < tem_3 and tem_1):
        print('La temperatura minima es {}' .format(tem_2))
    else:
        print('La temperatura minima es {}' .format(tem_3))

    print('Temperatura promedio:', temp_pro)

if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    #ej1()
    #ej2()
    #ej3()
    #ej4()
    ej5()

