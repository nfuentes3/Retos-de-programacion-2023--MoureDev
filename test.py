import random

minusculas = str('abcdefghijklmnñopqrstuvwxyz')
mayusculas = str(minusculas.upper())
numeros = str('1234567890')
simbolos = str('@!-.,?¡¿)((/&%')



def password_generator():
    criterio = ''
    long = int(input('Longitud: '))

    minus = input('Minusculas? Y/N: ')
    if minus == 'y':
        criterio += minusculas
    mayus = input('Mayusculas? Y/N: ')
    if mayus == 'y':
        criterio += mayusculas
    nums = input('Numeros? Y/N: ')
    if nums == 'y':
        criterio += (numeros)
    simbols = input('Simbolos? Y/N: ')
    if simbols == 'y':
        criterio += simbolos

    for password in range(1):
        pass_sample = random.sample(criterio, long)
        final_pass = ''.join(pass_sample)
        print(final_pass)

password_generator()