'''
Desarrolle un algoritmo que permita leer tres valores y almacenarlos en las variables A, B y C respectivamente. El algoritmo debe imprimir cual es el mayor y cual es el menor. Recuerde constatar que los tres valores introducidos por el teclado sean valores distintos. Presente un mensaje de alerta en caso de que se detecte la introducción de valores iguales.

'''

print('Escribe 3 números diferentes a continuación...')
print('Recuerda que ninguún valor debe ser igual')

a = float(input('Escribe el primer número 👉 '))
b = float(input('Escribe el segundo número 👉 '))
c = float(input('Escribe el tercer número 👉 '))
d = float(input('Escribe el tercer número 👉 '))


if a == b or a == c or a == d or b == c or b == d or c == d:
    print('uno o dos valores son iguales, por favor intoducir valores distintos')
    
else:
    #A
    if a > b and a > c and a > d:
        max = a
        var_max = 'a'
        if b > c and b > d:
            med_1 = b
            var_med_1 = 'b'
            if c > d:
                med_2 = c
                var_med_2 = 'c'
                min = d
                var_min = 'd'
            else:
                med_2 = d
                var_med_2 = 'd'
                min = c
                var_min = 'c'
        elif c > b and c > d:
            med_1 = c
            var_med_1 = 'c'
            if b > d:
                med_2 = b
                var_med_2 = 'b'
                min = d
                var_min = 'd'
            else:
                med_2 = d
                var_med_2 = 'd'
                min = b
                var_min = 'b'
        else:
            med_1 = d
            var_med_1 = 'd'
            if b > c:
                med_2 = b
                var_med_2 = 'b'
                min = c
                var_min = 'c'
            else:
                med_2 = c
                var_med_2 = 'c'
                min = b
                var_min = 'b'
    #B    
    elif b > a and b > c and b > d:
        max = b
        var_max = 'b'
        if a > c and a > d:
            med_1 = a
            var_med_1 = 'a'
            if c > d:
                med_2 = c
                var_med_2 = 'c'
                min = d
                var_min = 'd'
            else:
                med_2 = d
                var_med_2 = 'd'
                min = c
                var_min = 'c'
        elif c > a and c > d:
            med_1 = c
            var_med_1 = 'c'
            if a > d:
                med_2 = a
                var_med_2 = 'a'
                min = d
                var_min = 'd'
            else:
                med_2 = d
                var_med_2 = 'd'
                min = a
                var_min = 'a'
        else:
            med_1 = d
            var_med_1 = 'd'
            if a > c:
                med_2 = a
                var_med_2 = 'a'
                min = c
                var_min = 'c'
            else:
                med_2 = c
                var_med_2 = 'c'
                min = a
                var_min = 'a'
    #C
    if c > b and c > a and c > d:
        max = c
        var_max = 'c'
        if b > a and b > d:
            med_1 = b
            var_med_1 = 'b'
            if a > d:
                med_2 = a
                var_med_2 = 'a'
                min = d
                var_min = 'd'
            else:
                med_2 = d
                var_med_2 = 'd'
                min = a
                var_min = 'a'
        elif a > b and a > d:
            med_1 = a
            var_med_1 = 'a'
            if b > d:
                med_2 = b
                var_med_2 = 'b'
                min = d
                var_min = 'd'
            else:
                med_2 = d
                var_med_2 = 'd'
                min = b
                var_min = 'b'
        else:
            med_1 = d
            var_med_1 = 'd'
            if b > a:
                med_2 = b
                var_med_2 = 'b'
                min = a
                var_min = 'a'
            else:
                med_2 = a
                var_med_2 = 'a'
                min = b
                var_min = 'b'
    #D
    else:
        max = d
        var_max = 'd'
        if b > c and b > a:
            med_1 = b
            var_med_1 = 'b'
            if c > a:
                med_2 = c
                var_med_2 = 'c'
                min = a
                var_min = 'a'
            else:
                med_2 = a
                var_med_2 = 'a'
                min = c
                var_min = 'c'
        elif c > b and c > a:
            med_1 = c
            var_med_1 = 'c'
            if b > a:
                med_2 = b
                var_med_2 = 'b'
                min = a
                var_min = 'a'
            else:
                med_2 = a
                var_med_2 = 'a'
                min = b
                var_min = 'b'
        else:
            med_1 = a
            var_med_1 = 'a'
            if b > c:
                med_2 = b
                var_med_2 = 'b'
                min = c
                var_min = 'c'
            else:
                med_2 = c
                var_med_2 = 'c'
                min = b
                var_min = 'b'

#Imprimir resultado final    
    print('')
    print('*' * 20)
    print('')
    print('El número más grande es', max, ' de la variable', var_max)
    print('')
    print('El número mediano es', med_1, ' de la variable', var_med_1)
    print('')
    print('El número mediano es', med_2, ' de la variable', var_med_2)
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