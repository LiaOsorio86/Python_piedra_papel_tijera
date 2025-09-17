nombrejugador1= input('Ingrese el Nombre del Jugador 1: ')
nombrejugador2= input('Ingrese el Nombre del Jugador 2: ')

seguir='s'

while seguir.lower() == 's':
    jugador1= input(f'{nombrejugador1}, que elegis? piedra - papel - tijera?: ')
    jugador2= input(f'{nombrejugador2}, que elegis? piedra - papel - tijera?: ')

    while jugador1==jugador2:
        print ('Ha sido un empate, vuelvan a intentar')
        jugador1= input(f'{nombrejugador1}, que elegis? piedra - papel - tijera?: ')
        jugador2= input(f'{nombrejugador2}, que elegis? piedra - papel - tijera?: ')

    if (jugador1 == 'piedra' and jugador2 == 'tijera') or\
       (jugador1=='tijera' and jugador2=='papel')or\
       (jugador1=='papel' and jugador2=='piedra'):
        print (nombrejugador1, 'ha ganado')
    else: 
        print (nombrejugador2, 'ha ganado')
        
    seguir= input ('Seguimos jugando? S/N: ')

print ('Ha finalizado el juego!')




