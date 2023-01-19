"""
 * Escribe un programa que muestre cómo transcurre un juego de tenis y quién lo ha ganado.
 * El programa recibirá una secuencia formada por "P1" (Player 1) o "P2" (Player 2), según quien
 * gane cada punto del juego.
 * 
 * - Las puntuaciones de un juego son "Love" (cero), 15, 30, 40, "Deuce" (empate), ventaja.
 * - Ante la secuencia [P1, P1, P2, P2, P1, P2, P1, P1], el programa mostraría lo siguiente:
 *   15 - Love
 *   30 - Love
 *   30 - 15
 *   30 - 30
 *   40 - 30
 *   Deuce
 *   Ventaja P1
 *   Ha ganado el P1
 * - Si quieres, puedes controlar errores en la entrada de datos.   
 * - Consulta las reglas del juego si tienes dudas sobre el sistema de puntos.   
"""
#Inicializando las variables
player_one = 0
player_two = 0

#Creamos el diccionario con los puntos == valor
points = {
    0 : 'Love',
    1 : '15',
    2 : '30',
    3 : '40',
    4 : 'Game',
    5 : 'Ventaja'
}
print('El juego ha comenzado!!!')
print(f'Puntuacion actual: \n* Jugador 1 = {player_one} / * Jugador 2 = {player_two}')
print('-------------------------------------------------------------')


#Definimos funcion para la eleccion del ganador
while player_one < 4 and player_two < 4:
    print('Quien fue el ganador del punto?')
    print('1) Jugador 1\n2) Jugador 2')
    point_winner = input('Seleccione la opcion: ')
    if point_winner == '1':
        player_one += 1
    elif point_winner == '2':
        player_two += 1
    else:
        print('Ingreso un valor incorrecto.')
    print(f'Puntuacion actual: \n* Jugador 1 [ {points[player_one]} / {points[player_two]} ] * Jugador 2')
    print('-------------------------------------------------------------')
    if player_one >= 4 and player_two >= 3:
        print('Ganador el Jugador 1!!!')
    elif player_two >= 4 and player_one >= 3:
        print('Ganador el jugador 2!!!')
    elif player_one == 4 and player_two == 4:
        print(f'Puntuacion actual: \n* Jugador 1 [ Deuce ] * Jugador 2')
