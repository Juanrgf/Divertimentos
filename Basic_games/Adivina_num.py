''' Programa interactivo (en consola) que consiste en adivinar un número
aleatorio entre dos cotas dadas por el usuario '''

import random

print('Vamos a jugar a adivinar el número que estoy pensando. Dame dos números:')

cota_inf = int(input('Selecciona el número mínimo: '))
cota_sup = int(input('Selecciona el número máximo: '))

print(f'El número que estoy pensando está entre {cota_inf} y {cota_sup}')
print('¡A adivinar!')

num = random.randint(cota_inf, cota_sup)
intentos = int(input('¿Cuántos intentos crees requerir?: '))
i = 1

while i <= intentos:
    pred = int(
        input(f'Adivina el número ({intentos-i} intentos restantes): '))
    if pred == num:
        print(f'¡Acertaste! Y solo te tomó {i} intentos')
        break
    else:
        if pred > num:
            print(f'El número que estoy pensando es más pequeño que {pred}')
        else:
            print(f'El número que estoy pensando es más grande que {pred}')
        i += 1

    if i == intentos:
        res = input(
            f'Te has quedado sin intentos. ¿Quieres otros {intentos}?:[y/n] ')
        if res == 'y':
            i = 1
        else:
            print(
                f'Has perdido. El número en el que estaba pensado era {num}')
            break
