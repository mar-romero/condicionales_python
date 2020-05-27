#!/usr/bin/env python
'''
Condicionales [Python]
Ejercicios de práctica
---------------------------
Autor: Inove Coding School
Version: 1.1
 
Descripcion:
Programa creado para que practiquen los conocimietos adquiridos durante la semana
'''

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.1"

def ej1():
    # Ejercicios de práctica con números

    '''
    Realice un programa que solicite por consola 2 números
    Calcule la diferencia entre ellos e informe por pantalla
    si el resultado es positivo, negativo o cero.
        
    '''
    numero_1 = int(input('Ingrese el primer número:'))

    numero_2 = int(input('Ingrese el segundo número:'))
    
    resta = (numero_1 - numero_2)
    
    if (resta >= 1):
        print('El resultado es positivo')
    
    elif (resta == 0):
        print('El resultado es 0')
    
    else:
        print('El resultado es negativo')

def ej2():
# Ejercicios de práctica con números

    '''
    Realice un programa que solicite el ingreso de tres números
    enteros, y luego en cada caso informe si el número es par
    o impar.
    Para cada caso imprimir el resultado en pantalla.
    
    '''

    numero_1 = int(input('Ingrese el primer número:\n'))

    numero_2 = int(input('Ingrese el segundo número:\n'))
    
    numero_3 = int(input('Ingrese el tercer número:\n'))
    
    par_1 = (numero_1 % 2)
    par_2 = (numero_2 % 2)
    par_3 = (numero_3 % 2)
    
    if (par_1 == 0):
        print('{} es par'.format(numero_1))
    else:
        print( '{} es impar'.format(numero_1))
    if (par_2 == 0):
        print('{} es par'.format(numero_2))
    else:
        print( '{} es impar'.format(numero_2))
    if (par_3 == 0):
        print('{} es par'.format(numero_3))
    else:
        print( '{} es impar'.format(numero_3))

def ej3():
    # Ejercicios de práctica con números

    '''
    Realice una calculadora, se ingresará por línea de comando dos números
    Luego se ingresará como tercera entrada al programa el símbolo de la operación
    que se desea ejecutar
    - Suma (+)
    - Resta (-)
    - Multiplicación (*)
    - División (/)
    - Exponente/Potencia (**)

    Se debe efectuar el cálculo correcto según la operación ingresada por consola
    Imprimir en pantalla la operación realizada y el resultado
    

    '''

    num_1 = float(input('Ingrese el primer número:\n'))

    num_2 = float(input('Ingrese el segundo número:\n'))

    ope_1 = str(input('Ingrese la la operacion que desea:\n'))
    
    suma = num_1 + num_2
    res = num_1 - num_2
    mul = num_1 * num_2
    div = num_1 / num_2
    pot = num_1 ** num_2

    if (ope_1 == '+') :
        print('{} es el resultado' .format(suma))
    elif (ope_1 == '-') :
        print('{} es el resultado' .format(res))
    elif (ope_1 == "*") :
        print('{} es el resultado' .format(mul))
    elif (ope_1 == '/'):
        print('{} es el resultado' .format(div))
    elif (ope_1 == '**') :
        print('{} es el resultado' .format(pot))
    else :
        print('No es una operacion mapalatica')
        

    

    

def ej4():
    # Ejercicios de práctica con cadenas
    
    '''
    Realice un programa que solicite por consola 3 palabras cualesquiera
    Luego el programa debe consultar al usuario como quiere ordenar las palabras
    1 - Ordenar por orden alfabético (usando el operador ">")
    2 - Ordenar por cantidad de letras (longitud de la palabra)

    Si se ingresa "1" por consola se deben ordenar las 3 palabras por orden alfabético
    e imprimir en pantalla de la mayor a la menor

    Si se ingresa "2" por consola se deben ordenar las 3 palabras por cantidad de letras
    e imprimir en pantalla de la mayor a la menor

    '''
    pal_1 = str(input('Ingrese 3 palabra que desea:\n'))
    pal_1.split(" " and "," and ", ")
    or_1 = int(input ('Quiere ordenar las palabras alfabeticamente o por cantidad de letras: 1 o 2\n'))
    pal_2,pal_3,pal_4 = pal_1.split(" " and "," and ", ")
    if (or_1 == 1):

    


    input
if __name__ == '__main__':
    print("Ejercicios de práctica")
    #ej1()
    #ej2()
    #ej3()
    ej4()
