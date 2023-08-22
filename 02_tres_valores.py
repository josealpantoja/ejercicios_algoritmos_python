'''
Desarrolle un algoritmo que permita leer tres valores y almacenarlos en las variables A, B y C respectivamente. El algoritmo debe imprimir cual es el mayor y cual es el menor. Recuerde constatar que los tres valores introducidos por el teclado sean valores distintos. Presente un mensaje de alerta en caso de que se detecte la introducción de valores iguales.

'''

print('Escribe 3 números diferentes a continuación...')
print('Recuerda que ninguún valor debe ser igual')

a = float(input('Escribe el primer número 👉 '))
b = float(input('Escribe el segundo número 👉 '))
c = float(input('Escribe el tercer número 👉 '))


if a == b or a == c or b == c:
    print('uno o dos valores son iguales, por favor intoducir valores distintos')
    
else:
    if a > b and a > c:
        max = a
        var_max = 'a'
        if b > c:
            med = b
            var_med = 'b'
            min = c
            var_min = 'c'
        else:
            med = c
            var_med = 'c'
            min = b
            var_min = 'b'

    elif b > a and b > c:
        max = b
        var_max = 'b'
        if a > c:
            med = a
            var_med = 'a'
            min = c
            var_min = 'c'
        else:
            med = c
            var_med = 'c'
            min = a
            var_min = 'a'

    else:
        max = c
        var_max = 'c'
        if a > b:
            med = a
            var_med = 'a'
            min = b
            var_min = 'b'
        else:
            med = b
            var_med = 'b'
            min = a
            var_min = 'a'
    
    print('')
    print('*' * 20)
    print('')
    print('El número más grande es', max, ' de la variable', var_max)
    print('')
    print('El número mediano es', med, ' de la variable', var_med)
    print('')
    print('El número más chico es', min, ' de la variable', var_min)
    print('')
    print('*' * 20)
    print('')



'''
VERSION ANTERIOR SOLO PARA ESTUDIO

if a == b or a == c or b == c:
    print('uno o dos valores son iguales, por favor intoducir valores distintos')
    
else:
    if a > b:
        if a > c:
            # a es max
            max = a
            if b > c:
                med = b
                min = c
                # b es med
            else:
                med = c
                min = b
                # c es med

        else:
            # a es med
            med = a
            if b > c:
                max = b
                min = c
                # c es min
            else:
                max = c
                min = b
                # b es min
    else:
        if a < c:
            min = a
            if b < c:
                max = c
                med = b
            else:
                max = b
                med = c
        else:
            max = b
            med = a
            min = c

    print('')
    print('*' * 20)
    print('')
    print('El número más grande es', max)
    print('')
    print('El número mediano es', med)
    print('')
    print('El número más chico es', min)
    print('')
    print('*' * 20)
    print('')
'''