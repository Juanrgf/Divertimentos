''' Programa interactivo (en consola) que simula el juego del ahorcado '''
import random

print('Vamos a jugar el juego del ahorcado. Para ello déjame pensar en una palabra')
words = ['caballo', 'abeja', 'edificio', 'pizarra']

word = random.choice(words)
n = len(word)
print('¡Listo! ya seleccioné una palabra.')
intentos = int(input(f'La palabra seleccionada es de {n} letras, ¿cuántos intentos crees requerir? '))

while intentos < n:
    print(f'¡Requieres más intentos!')
    intentos = int(input(f'La palabra seleccionada es de {n} letras, ¿cuántos intentos crees requerir? '))

print('¡A jugar!')

i = 1
cadena = ['_' for i in range(n)]

while i <= intentos:
    letra = input(f'Dame una letra ({intentos-i} intentos restantes): ')
    if letra in word:
        indice = [ind for ind, val in enumerate(word) if val == letra]
        for ind in indice:
            cadena[ind] = letra
            cadena_str = ''.join(cadena)
        print(f'¡Acertaste!: {cadena_str}')
        if cadena_str == word:
            print(f'¡Has ganado! La palabra era {word} y lo lograste con solo {i} intento(s)')
            break
    else:
        print('Error, intenta nuevamente')
        i +=1
    if i == intentos:
        res = input(f'Te has quedado sin intentos. ¿Quieres otros {intentos}?:[y/n] ')
        if res == 'y':
            i = 1
        else:
            print(f'Has perdido. La palabra que pensé era {word}')
            break