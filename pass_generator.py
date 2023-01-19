""" * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros:
 * - Longitud: Entre 8 y 16.
 * - Con o sin letras mayúsculas.
 * - Con o sin números.
 * - Con o sin símbolos.
 * (Pudiendo combinar todos estos parámetros entre ellos)"""

import random

#Inicializamos las variables con los caracteres
minusculas = str('abcdefghijklmnñopqrstuvwxyz')
mayusculas = str(minusculas.upper())
numeros = str('1234567890')
simbolos = str('@!-.,?¡¿)((/&%')

print('Bienvenido al generador de claves!')
print('Por favor, seleccione los criterios para la generacion de la clave:')
print('------------------------------------------------------------------')

#Creamos la funcion para generar la contraseña segun los criterios
def password_generator():
    criterio = ''
    long = int(input('\nCual es la longitud que desea?(Entre 8 y 16 caracteres): ')) #Longitud

    minus = input('\nDesea que contenga minusculas? Y/N: ') #Minusculas
    minus = minus.lower()
    if minus == 'y':
        criterio += minusculas

    mayus = input('\nDesea que contenga mayusculas? Y/N: ') #Mayusculas
    mayus = mayus.lower()
    if mayus == 'y':
        criterio += mayusculas

    nums = input('\nDesea que contenga numeros? Y/N: ') #Numeros
    nums = nums.lower()
    if nums == 'y':
        criterio += (numeros)

    simbols = input('\nDesea que contenga simbolos? Y/N: ') #Simbolos
    simbols = simbols.lower()
    if simbols == 'y':
        criterio += simbolos

    #Generador aleatorio de contraseñas segun criterios.
    for password in range(1):
        pass_sample = random.sample(criterio, long)
        final_pass = ''.join(pass_sample)
        print(f'Su contraseña generada es la siguiente: {final_pass}')

password_generator()